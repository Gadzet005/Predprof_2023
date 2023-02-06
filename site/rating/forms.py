from django import forms

from rating.models import SiteRating
from core.forms import FormStyleMixin


class RatingForm(forms.ModelForm, FormStyleMixin):
    class Meta:
        model = SiteRating
        fields = ('rating', 'feedback')
