from django.urls import path

from rating.views import CreateRatingView, UpdateRatingView


app_name = 'rating'

urlpatterns = [
    path('site/<int:site_id>/add-rating/', CreateRatingView.as_view(), name='create'),
    path('site/<int:site_id>/update-rating/', UpdateRatingView.as_view(), name='update'),
]
