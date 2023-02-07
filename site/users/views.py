from django.views.generic import CreateView, UpdateView
import django.contrib.auth.views as AuthViews
from django.urls.base import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string

from users import forms
from users.models import User


class RegisterView(CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'base_form.html'
    extra_context = {
        'page_title': 'Регистрация',
        'button_text': 'Создать аккаунт',
        'form_title': 'Регистрация',
    }
    success_url = reverse_lazy('common:home')
    success_message = (
        'Вы <strong>успешно</strong> зарегистрировались'
    )

    def form_valid(self, form):
        result = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.add_message(
            self.request, messages.SUCCESS, self.success_message,
            extra_tags='alert-success'
            )
        return result


class LoginView(AuthViews.LoginView):
    form_class = forms.LoginUserForm
    template_name = 'users/login_form.html'
    extra_context = {
        'page_title': 'Вход',
        'button_text': 'Войти',
        'form_title': 'Вход в аккаунт',
    }


class LogoutView(LoginRequiredMixin, AuthViews.LogoutView):
    template_name = 'users/logout.html'


class ChangePasswordView(LoginRequiredMixin, AuthViews.PasswordChangeView):
    template_name = 'base_form.html'
    success_url = reverse_lazy('users:profile')
    form_class = forms.ChangeUserPasswordForm
    extra_context = {
        'page_title': 'Изменить пароль',
        'form_title': 'Изменить пароль',
        'button_text': 'Изменить'
    }

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            '<h6>Ваш пароль был успешно изменен.</h6>',
            extra_tags='alert-success'
            )
        return result


class ResetPasswordView(AuthViews.PasswordResetView):
    template_name = 'base_form.html'
    email_template_name = 'users/reset_password_email.html'
    from_email = settings.OWNER_EMAIL
    form_class = forms.ResetUserPasswordForm
    model = User
    success_url = reverse_lazy('common:home')
    extra_context = {
        'page_title': 'Восстановление пароля',
        'form_title': 'Восстановление пароля',
        'button_text': 'Восстановить'
    }

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(
            self.request, messages.INFO,
            render_to_string('users/messages/reset_password.html'),
            extra_tags='alert-primary'
            )
        return result


class PasswordResetConfirmView(AuthViews.PasswordResetConfirmView):
    template_name = 'base_form.html'
    form_class = forms.ResetUserPasswordConfirmForm
    success_url = reverse_lazy('users:login')
    extra_context = {
        'page_title': 'Сброс пароля',
        'form_title': 'Сброс пароля',
        'button_text': 'Изменить пароль'
    }

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            render_to_string('users/messages/password_reset_done.html'),
            extra_tags='alert-success'
            )
        return result


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.UpdateUserProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('users:profile')
    extra_context = {
        'page_title': 'Мой профиль',
        'button_text': 'Сохранить',
        'form_title': 'Профиль',
    }

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS,
            '<h6>Данные успешно сохранены</h6>',
            extra_tags='alert-success'
            )
        return super().form_valid(form)
