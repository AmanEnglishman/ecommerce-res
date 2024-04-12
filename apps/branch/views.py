from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView

from apps.branch.models import Branch, Booth
from apps.branch.serializers import BranchSerializer, BoothSerializer


class BranchListAPIView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchRetrieveAPIView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BootListAPIView(ListAPIView):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer


class BootRetrieveAPIView(RetrieveAPIView):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer
