from rest_framework import serializers
from django.db.models import Avg
from category.models import Category
from .models import *


class PostListSerializer(serializers.ModelSerializer):
    created_ad = serializers.DateTimeField(format='%d/%m/%y %H:%M:%S', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'description', 'category', 'video')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = PostImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     print(instance, '!!!!!!!!!!!!!!!')
    #     repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
    #     return repr

#
# class PostDetailSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.email')
#     category = serializers.PrimaryKeyRelatedField(
#         required=True, queryset=Category.objects.all())
#
#     class Meta:
#         model = Post
#         fields = '__all__'

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
    #     repr['rating_count'] = instance.reviews.count()
    #     return repr


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = PostImage
        fields = '__all__'
