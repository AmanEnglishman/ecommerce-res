from django.urls import path
from .views import UserRegisterAPIView, UserListAPIView, LoginAPIView, UserDetailAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
]