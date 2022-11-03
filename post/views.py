from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, response, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action
# from . models import Post
#
# from . import serializers
from .serializers import *



#
# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return serializers.PostListSerializer
#         return serializers.PostDetailSerializer
#
#     def get_permissions(self):
#         if self.action in ('update', 'partial_update', 'destroy'):
#             return [permissions.IsAuthenticated()]
#         return [permissions.IsAuthenticatedOrReadOnly()]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     # api/v1/products/<id>/reviews/
#     @action(['GET', 'POST'], detail=True)
#     def reviews(self, request, pk):
#         post = self.get_object()
#         if request.method == 'GET':
#             reviews = post.reviews.all()
#         elif post.reviews.filter(owner=request.user).exists():
#             return response.Response('Вы уже оставляли отзыв!!', status=400)
#         data = request.data
#         # serializer = ReviewSerializer(data=data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save(owner=request.user, product=product)
#         # return response.Response(serializer.data, status=201)
#


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

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

    # def get_list_video(request):
    #     return render(request, 'video_hosting/home.html', {'video_list': Post.objects.all()})
    #
    # def get_video(request, pk: int):
    #     _video = get_object_or_404(Post, id=pk)
    #     return render(request, 'video_hosting/home.html', {'video': _video})



class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return{'request': self.request}
