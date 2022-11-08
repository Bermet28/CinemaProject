from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, response, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *


from django.views.generic import ListView
from post.models import Post


class MyPaginationClass(PageNumberPagination):
    page_size = 100
    def get_paginated_response(self, data):
        for i in range(self.page_size):
            text = data[i]['text']
            data[i]['text'] = text[:15] + '....'
        return super().get_paginated_response(data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = MyPaginationClass

    @action(detail=False, methods='GET')
    def own(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(owner=request.user)
        serializer = PostListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(created_ad__icontains=q))
        serializer = PostListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


def index(request):
    videos = Post.objects.all()
    return render(request, 'videos/index.html', context={'videos': videos})


class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return{'request': self.request}


class GenreYear:
    def get_genres(self):
        # нужно вместо поста прописать жанр
        return Post.objects.all()
        # нужно вместо пост прописать фильм
    def get_years(self):
        return Post.objects.filter(draft=False).values('created_ad')


class FilterView(GenreYear, ListView):
    def get_request(self):
        queryset = Post.objects.filter(
            Q(year__in=self.request.GET.get('created_ad')) |
            Q(genres__in=self.request.GET.get('title'))
        )
        return queryset