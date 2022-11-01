from rest_framework import serializers
from django.db.models import Avg
from category.models import Category
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Post
        fields = ('title', 'description', 'image')

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     print(instance, '!!!!!!!!!!!!!!!')
    #     repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
    #     return repr


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
    #     repr['rating_count'] = instance.reviews.count()
    #     return repr

