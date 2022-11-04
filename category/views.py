from django.shortcuts import render

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Category, Genre
from . import serializers
from .serializers import CategorySerializer, GenreSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_permissions(self):
    #     if self.action in ('retrieve', 'list'):
    #         return [permissions.AllowAny()]
    #     else:
    #         return [permissions.IsAdminUser()]


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
