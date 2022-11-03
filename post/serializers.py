from rest_framework import serializers
from django.db.models import Avg
from category.models import Category
from .models import *


class PostListSerializer(serializers.ModelSerializer):
    created_ad = serializers.DateTimeField(format='%d/%m/%y %H:%M:%S', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'description', 'category', 'video', 'created_ad')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = PostImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = PostImage
        fields = '__all__'