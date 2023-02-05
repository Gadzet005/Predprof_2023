from django import forms

from core.forms import FormStyleMixin
from catalog.models import Site


class CreateUserSiteForm(forms.ModelForm, FormStyleMixin):
    class Meta:
        model = Site
        fields = ('name', 'url', 'logo', 'description')
        widgets = {
            'url': forms.URLInput({'placeholder': 'https://www.google.com'})
        }


class UpdateUserSiteForm(forms.ModelForm, FormStyleMixin):
    class Meta:
        model = Site
        fields = ('name', 'url', 'logo', 'description')
        widgets = {
            'logo': forms.FileInput(),
        }
        labels = {
            'logo': 'Изменить логотип'
        }
