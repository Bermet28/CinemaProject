# from dataclasses import field
# from multiprocessing.context import SpawnContext
# from pyexpat import model
from rest_framework import serializers
from .models import Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()

    class Meta:
        model = Genre
        fields = '__all__'
