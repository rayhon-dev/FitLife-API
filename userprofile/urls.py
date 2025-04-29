from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('auth/signup/', views.RegisterView.as_view(), name='signup'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='logout')
]