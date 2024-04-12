from django.urls.conf import path

from .views import MenuAPIView

urlpatterns = [
    path('', MenuAPIView.as_view(), name='menu'),
]