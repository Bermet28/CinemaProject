from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.db.models import Q, Case, When
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import ListView
from rest_framework import viewsets, status, generics, response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import permissions
from account.permissions import IsAuthor
from post import serializers
from post.models import Post, Like, Notification
from post.serializers import PostListSerializer
from rating.serializers import ReviewSerializer
# import pandas as pd


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

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(created_ad__icontains=q))
        serializer = PostListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        elif self.action in ('create', 'add_to_liked', 'remove_from_liked', 'favorite_action'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        product = self.get_object()
        if request.method == 'GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if product.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв!!', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, product=product)
        return response.Response(serializer.data, status=201)

    @action(['DELETE'], detail=True)
    def remove_from_reviews(self, request, pk):
        movie = self.get_object()
        user = request.user
        if not user.review.filter(movie=movie).exists():
            return Response('You are not Review This Movie!', status=400)
        user.review.filter(movie=movie).delete()
        return Response('Your Review is Deleted!', status=204)

    @action(['POST'], detail=True)
    def add_to_liked(self, request, pk):
        post = self.get_object()
        user = request.user
        if user.liked.filter(post=post).exists():
            return Response('This Movie is Already Liked!', status=400)
        Like.objects.create(owner=user, post=post, )
        return Response('You Liked The Music', status=201)

    # /posts/<id>?remove_from_liked/
    @action(['DELETE'], detail=True)
    def remove_from_liked(self, request, pk):
        post = self.get_object()
        user = request.user
        if not user.liked.filter(post=post).exists():
            return Response('You Didn\'t Like This Music!', status=400)
        user.liked.filter(post=post).delete()
        return Response('Your Like is Deleted!', status=204)

    @action(['GET'], detail=True)
    def get_likes(self, request, pk):
        post = self.get_object()
        likes = post.likes.all()
        serializer = serializers.LikeSerializer(likes, many=True)
        return Response(serializer.data, status=200)


def index(request):
    videos = Post.objects.all()
    return render(request, 'videos/index.html', context={'videos': videos})


def ShowNotifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    template = loader.get_template('notification.html')
    context = {
        'notifications': notifications,
    }
    return HttpResponse(template.render(context, request))


def auth(request):
    return render(request, 'oauth.html')


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

# def get_similar(movie_name, rating, corr_matrix):
#     similar_ratings = corr_matrix[movie_name] * (rating - 2.5)
#     similar_ratings = similar_ratings.sort_values(ascending=False)
#     return similar_ratings
#
#
# def recommend(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     if not request.user.is_active:
#         raise Http404
#
#     movie_rating = pd.DataFrame(list(Myrating.objects.all().values()))
#
#     new_user = movie_rating.user_id.unique().shape[0]
#     current_user_id = request.user.id
#     # if new user not rated any movie
#     if current_user_id > new_user:
#         movie = Post.objects.get(id=19)
#         q = Myrating(user=request.user, movie=movie, rating=0)
#         q.save()
#
#     user_ratings = movie_rating.pivot_table(index=['user_id'], columns=['movie_id'], values='rating')
#     user_ratings = user_ratings.fillna(0, axis=1)
#     corr_matrix = user_ratings.corr(method='pearson')
#
#     user = pd.DataFrame(list(Myrating.objects.filter(user=request.user).values())).drop(['user_id', 'id'], axis=1)
#     user_filtered = [tuple(x) for x in user.values]
#     movie_id_watched = [each[0] for each in user_filtered]
#
#     similar_movies = pd.DataFrame()
#     for movie, rating in user_filtered:
#         similar_movies = similar_movies.append(get_similar(movie, rating, corr_matrix), ignore_index=True)
#
#     movies_id = list(similar_movies.sum().sort_values(ascending=False).index)
#     movies_id_recommend = [each for each in movies_id if each not in movie_id_watched]
#     preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(movies_id_recommend)])
#     movie_list = list(Post.objects.filter(id__in=movies_id_recommend).order_by(preserved)[:10])
#
#     context = {'movie_list': movie_list}
#     return render(request, 'recommend/recommend.html', context)
