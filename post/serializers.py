from rest_framework import serializers
from django.db.models import Avg
from .models import *


class PostListSerializer(serializers.ModelSerializer):
    created_ad = serializers.DateTimeField(format='%d/%m/%y %H:%M:%S', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


# class DirectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Director
#         fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields = "__all__"