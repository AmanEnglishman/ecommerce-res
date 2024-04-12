from django.urls import path
from .views import UserRegisterView, LoginAPIView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    # path('users/', UserListAPIView.as_view(), name='user-list'),
]