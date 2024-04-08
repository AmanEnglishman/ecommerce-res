from django.urls import path

from .views import BranchListAPIView, BranchCreateAPIView, BranchUpdateAPIView, BranchDestroyAPIView, BranchRetrieveAPIView

urlpatterns = [
    path('', BranchListAPIView.as_view(), name='branch-list'),
    path('create/', BranchCreateAPIView.as_view(), name='branch-create'),
    path('<int:pk>/', BranchRetrieveAPIView.as_view(), name='branch-retrieve'),
    path('update/<int:pk>/', BranchUpdateAPIView.as_view(), name='branch-update'),
    path('destroy/<int:pk>/', BranchDestroyAPIView.as_view(), name='branch-destroy'),

]