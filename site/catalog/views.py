from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from catalog.models import Site, UserSite
from catalog.forms import CreateUserSiteForm, UpdateUserSiteForm


class SiteListView(ListView):
    template_name = 'catalog/site_list.html'
    queryset = Site.objects.get_for_main_catalog()
    context_object_name = 'sites'
    paginate_by = 5


class UserSiteListView(LoginRequiredMixin, SiteListView):
    template_name = 'catalog/user_site_list.html'

    def get_queryset(self):
        return Site.objects.get_user_sites(self.request.user)


class CreateUserSiteView(LoginRequiredMixin, CreateView):
    template_name = 'base_form.html'
    success_url = reverse_lazy('catalog:user_list')
    form_class = CreateUserSiteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        UserSite.objects.create(site=self.object, user=self.request.user)
        return super().form_valid(form)


class SiteDetailView(DetailView):
    template_name = 'catalog/site_detail.html'
    pk_url_kwarg = 'site_id'
    context_object_name = 'site'

    def get_queryset(self):
        return Site.objects.enabled(self.request.user)


class UpdateUserSiteView(LoginRequiredMixin, UpdateView):
    template_name = 'base_form.html'
    pk_url_kwarg = 'site_id'
    form_class = UpdateUserSiteForm

    def get_queryset(self):
        return Site.objects.get_user_sites(self.request.user)


class DeleteUserSiteView(LoginRequiredMixin, DeleteView):
    template_name = 'catalog/delete_confirm.html'
    pk_url_kwarg = 'site_id'
    success_url = reverse_lazy('catalog:user_list')

    def get_queryset(self):
        return Site.objects.get_user_sites(self.request.user)
