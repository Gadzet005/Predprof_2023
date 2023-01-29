from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path(
        'change_password/', views.ChangePasswordView.as_view(),
        name='change_password'
        ),

    path(
        'reset_password/', views.ResetPasswordView.as_view(),
        name='reset_password'
        ),
    path(
        'reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
        name='reset_password_confirm'
        ),


    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
