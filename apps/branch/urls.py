from django.urls import path

from .views import BranchListAPIView, BranchRetrieveAPIView, BootListAPIView, BootRetrieveAPIView

urlpatterns = [
    path('', BranchListAPIView.as_view(), name='branch-list'),
    path('<int:pk>/', BranchRetrieveAPIView.as_view(), name='branch-retrieve'),
    path('boot/', BootListAPIView.as_view(), name='branch-list'),
    path('boot/<int:pk>/', BootRetrieveAPIView.as_view(), name='boot-list'),

]