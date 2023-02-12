from django.urls import path

from reports.views import ReportView


app_name = 'reports'

urlpatterns = [
    path('report/', ReportView.as_view(), name='report'),
]
