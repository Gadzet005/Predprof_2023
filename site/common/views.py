from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'common/index.html'
