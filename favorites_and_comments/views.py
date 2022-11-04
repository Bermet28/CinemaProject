from django.contrib.auth import get_user_model
from rest_framework import generics, response, permissions, viewsets
from . import serializers
from account.permissions import IsAuthor
from .models import Comment, Favorites

User = get_user_model()


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthor,)


class FavoritesListCreateView(generics.ListCreateAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoritesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)


class FavoritesDeleteView(generics.DestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthor,)
