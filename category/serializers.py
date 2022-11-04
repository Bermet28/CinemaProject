# from dataclasses import field
# from multiprocessing.context import SpawnContext
# from pyexpat import model
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'
