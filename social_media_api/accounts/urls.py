# accounts/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='account-register'),
    path('login/', LoginView.as_view(), name='account-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
