from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from reports.forms import ReportForm


class ReportView(LoginRequiredMixin, CreateView):
    template_name = 'base_form.html'
    form_class = ReportForm
    success_url = '/catalog'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.save()
        return super().form_valid(form)
