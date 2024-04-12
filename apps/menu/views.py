from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.menu.models import Menu
from apps.menu.serializers import MenuSerializer


class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MenuSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title',)
