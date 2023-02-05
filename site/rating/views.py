from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

from rating.forms import CreateRatingForm
from rating.models import SiteRating
from catalog.models import Site


class CreateRatingView(LoginRequiredMixin, CreateView):
    template_name = 'base_form.html'
    form_class = CreateRatingForm
    pk_url_kwarg = 'site_id'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            site_id = self.kwargs.get(self.pk_url_kwarg)
            self.site = get_object_or_404(Site, pk=site_id, is_on_catalog=True)

            rating = SiteRating.objects.get_user_rating(self.site, self.request.user)
            # Если пользователь уже оценил сайт, то возвращаем 404
            if rating:
                return HttpResponseNotFound()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        rating = form.save(commit=False)
        rating.user = self.request.user
        rating.site = self.site
        rating.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.site.get_absolute_url()
