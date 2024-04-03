from rest_framework import generics, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .permissions import AnonPermission
from .serializers import CustomUserSerializer, MyTokenSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenSerializer
