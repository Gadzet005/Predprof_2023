from django import forms

from catalog.models import Site
from reports.models import SiteReports
from core.forms import FormStyleMixin


class ReportForm(forms.ModelForm, FormStyleMixin):
    urls = [(i.url, i.url) for i in Site.objects.filter(is_on_catalog=True)]
    print(urls)

    url = forms.ChoiceField(
        choices=urls,
    )

    class Meta:
        model = SiteReports
        fields = ('url', 'region', 'problem')
