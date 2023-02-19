from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from users.models import User
from config.settings import TELEGRAM_TOKEN as TOKEN


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        LOGIN, PASSWORD, = 1, 2

        async def start(update, context) -> int:
            await update.message.reply_text(
                "Прветствуем Вас в нашем телеграм боте. "
                "Для того чтобы подписаться на оповещения об изменении статуса отслеживаемых Вам сайтов, "
                "Вам нужно авторизоваться.",
            )
            await update.message.reply_text(
                "Введите Ваш логин:",
            )

            return LOGIN

        async def get_login(update, context) -> int:
            context.user_data['login'] = update.message.text
            await update.message.reply_text(
                "Введите пароль:",
            )

            return PASSWORD

        @sync_to_async
        def get_user(login='', chat_id=0):
            if login:
                return User.objects.get(email=login)
            else:
                return User.objects.get(chat_id=chat_id)

        async def get_password_and_summarize(update, context) -> int:
            context.user_data['password'] = update.message.text
            try:
                user = await get_user(login=context.user_data['login'])
            except ObjectDoesNotExist:
                await update.message.reply_text(
                    "Неверный логин или пароль. Повторите попытку заново.",
                )
                await update.message.reply_text(
                    "Введите Ваш логин:",
                )
                return LOGIN
            if user.check_password(context.user_data['password']):
                await update.message.reply_text(
                    "Авторизация завершена. Оповещения включены",
                )
                user.chat_id = update.message.chat.id
                await sync_to_async(user.save)()
            else:
                await update.message.reply_text(
                    "Неверный логин или пароль. Повторите попытку заново.",
                )
                await update.message.reply_text(
                    "Введите Ваш логин:",
                )
                return LOGIN
            return ConversationHandler.END

        async def cancel(update, context) -> int:
            await update.message.reply_text(
                "Авторизация прервана."
            )

            return ConversationHandler.END

        async def unsubscribe(update, context):
            try:
                user = await get_user(chat_id=update.message.chat.id)
                user.chat_id = 0
                await sync_to_async(user.save)()
                await update.message.reply_text(
                    "Вы успешно отписались.",
                )
            except ObjectDoesNotExist:
                await update.message.reply_text(
                    "Отписаться не получилось: Вы еще не авторизовались.",
                )

        application = Application.builder().token(TOKEN).build()

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                LOGIN: [MessageHandler(filters.TEXT, get_login)],
                PASSWORD: [MessageHandler(filters.TEXT, get_password_and_summarize)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )

        application.add_handler(conv_handler)

        application.add_handler(CommandHandler("unsubscribe", unsubscribe))
        application.run_polling()
