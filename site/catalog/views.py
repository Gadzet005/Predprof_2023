from django.views.generic import ListView, DetailView

from catalog.models import Site


class SiteListView(ListView):
    template_name = 'catalog/site_list.html'
    queryset = Site.objects.filter(is_on_catalog=True)
    context_object_name = 'sites'
    paginate_by = 5


class SiteDetailView(DetailView):
    template_name = 'catalog/site_detail.html'
    model = Site
    pk_url_kwarg = 'site_id'
    context_object_name = 'site'
