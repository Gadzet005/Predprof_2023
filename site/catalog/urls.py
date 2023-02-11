from django.urls import path

from catalog.views import SiteListView, SiteDetailView

app_name = 'catalog'

urlpatterns = [
    path('', SiteListView.as_view(), name='list'),
    path('site/<int:site_id>/', SiteDetailView.as_view(), name='detail'),
]
