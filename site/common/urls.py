from django.urls import path

from common.views import HomePageView

app_name = 'common'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
