from django.urls import path

from reports.views import ReportView


app_name = 'reports'

urlpatterns = [
    path('create/<int:site_id>/', ReportView.as_view(), name='create'),
]
