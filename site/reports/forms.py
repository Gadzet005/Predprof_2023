from django import forms

from reports.models import SiteReport
from core.forms import FormStyleMixin


class ReportForm(forms.ModelForm, FormStyleMixin):
    class Meta:
        model = SiteReport
        fields = ('region', 'problem')
        widgets = {
            'problem': forms.Textarea(attrs={'placeholder': 'Описание проблемы'})
        }
