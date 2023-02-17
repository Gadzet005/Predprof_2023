from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages

from catalog.models import Site
from reports.forms import ReportForm


class ReportView(LoginRequiredMixin, CreateView):
    template_name = 'base_form.html'
    form_class = ReportForm
    success_url = reverse_lazy('catalog:list')

    def dispatch(self, request, *args, **kwargs):
        site_id = self.kwargs.get('site_id')
        self.site = get_object_or_404(
            Site.objects.enabled(self.request.user), pk=site_id
            )

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.site = self.site
        report.save()

        messages.add_message(
            self.request, messages.INFO,
            'Ваша заявка была отправлена и будет рассмотрена в ближайшее время',
            extra_tags='alert-primary'
            )

        return super().form_valid(form)
