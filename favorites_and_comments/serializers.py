from rest_framework import serializers
from .models import Comment, Favorites
from post.models import Post, Like


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = ('owner', 'body', 'music')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'track', 'image',)


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('music',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['music'] = MusicSerializer(instance.music).data
        return repr


class CommentListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'music',)


class CommentDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = '__all__'
