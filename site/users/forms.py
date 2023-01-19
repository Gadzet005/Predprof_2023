import django.contrib.auth.forms as UserForms
from django import forms

from users.models import User
from core.forms import FormStyleMixin


class RegisterUserForm(UserForms.UserCreationForm, FormStyleMixin):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class LoginUserForm(UserForms.AuthenticationForm, FormStyleMixin):
    username = forms.EmailField(label='Почта')


class ChangeUserPasswordForm(UserForms.PasswordChangeForm, FormStyleMixin):
    pass


class ResetUserPasswordForm(UserForms.PasswordResetForm, FormStyleMixin):
    pass


class ResetUserPasswordConfirmForm(
    UserForms.AdminPasswordChangeForm, FormStyleMixin
):
    pass


class UpdateUserProfileForm(forms.ModelForm, FormStyleMixin):
    class Meta:
        model = User
        fields = ('username', 'email', 'birthday_date', 'avatar')

        widgets = {
            'avatar': forms.FileInput(),
            'birthday_date': forms.TextInput(attrs={'type': 'date'})
        }
        labels = {
            'avatar': 'Изменить аватарку'
        }
