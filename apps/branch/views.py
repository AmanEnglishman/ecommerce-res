from django.shortcuts import render

from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView

from apps.branch.models import Branch
from apps.branch.serializers import BranchSerializer


class BranchListAPIView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDestroyAPIView(DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchUpdateAPIView(UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchCreateAPIView(CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchRetrieveAPIView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
