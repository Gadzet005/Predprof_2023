from django.urls import path

from rating.views import CreateRatingView


app_name = 'rating'

urlpatterns = [
    path('site/<int:site_id>/add-rating/', CreateRatingView.as_view(), name='create'),
]
