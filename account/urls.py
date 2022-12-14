from django import views
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

# from .views import SocialLoginView

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('active/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('forgot/', views.ForgotPasswordView.as_view()),
    path('restore/', views.RestorePasswordView.as_view()),
    path('follow-spam/', views.FollowSpamApi.as_view()),

]
