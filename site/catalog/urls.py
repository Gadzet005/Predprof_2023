from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.SiteListView.as_view(), name='list'),
    path('my/', views.UserSiteListView.as_view(), name='user_list'),

    path('site/<int:site_id>/', views.SiteDetailView.as_view(), name='detail'),
    path('create/', views.CreateUserSiteView.as_view(), name='create'),
    path('site/<int:site_id>/update/', views.UpdateUserSiteView.as_view(), name='update'),
    path('site/<int:site_id>/delete/', views.DeleteUserSiteView.as_view(), name='delete'),
]
