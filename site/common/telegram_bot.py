from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)
from requests import get
import os

from site.users import User
from django.core.exceptions import ObjectDoesNotExist


TOKEN = os.environ['TELEGRAM_TOKEN']

LOGIN, PASSWORD, = 1, 2


async def task(site_name, cur_code, recipients_list):
    if cur_code < 400:
        for recipient in recipients_list:
            chat_id = User.objects.get(email=recipient).chat_id
            text = f'Ресурс {site_name} сейчас доступен'
            r = get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

    else:
        for recipient in recipients_list:
            chat_id = User.objects.get(email=recipient).chat_id
            text = f'Ресурс {site_name} сейчас не доступен'
            r = get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')


async def start(update, context) -> int:
    await update.message.reply_text(
        "Прветствуем Вас в нашем телеграм боте. "
        "Для того чтобы подписаться на оповещения об изменении статуса отслеживаемых Вам сайтов, "
        "Вам нужно авторизоваться.",
    )
    update.message.reply_text(
        "Введите Ваш логин:",
    )

    return LOGIN


async def get_login(update, context) -> int:
    context.user_data['login'] = update.message.text
    await update.message.reply_text(
        "Введите пароль:",
    )

    return PASSWORD


async def get_password_and_summarize(update, context) -> int:
    context.user_data['password'] = update.message.text
    try:
        user = User.objects.get(email=context.user_data['login'])
    except ObjectDoesNotExist:
        update.message.reply_text(
            "Неверный логин или пароль. Повторите попытку заново.",
        )
        update.message.reply_text(
            "Введите Ваш логин:",
        )
        return LOGIN
    if user.check_password(context.user_data['password']):
        update.message.reply_text(
            "Авторизация завершена. Оповещения включены",
        )
        user.chat_id = update.message.chat.id
    else:
        update.message.reply_text(
            "Неверный логин или пароль. Повторите попытку заново.",
        )
        update.message.reply_text(
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
        user = User.objects.get(chat_id=update.message.chat.id)
        user.chat_id = ''
        update.message.reply_text(
            "Вы успешно отписались.",
        )
    except ObjectDoesNotExist:
        update.message.reply_text(
            "Отписаться не получилось: Вы еще не авторизовались.",
        )


def bot_starter():
    application = Application.builder().token("TOKEN").build()

    application.job_queue.run_repeating(task, 600)
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
    application.start_polling()


if __name__ == '__main__':
    bot_starter()