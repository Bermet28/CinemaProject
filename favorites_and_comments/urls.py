from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import CommentListCreateView

router = DefaultRouter()


urlpatterns =[
    path('',  include(router.urls)),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()),
    path('favorites/', views.FavoritesListCreateView.as_view()),
    path('favorites/<int:pk>', views.CommentDetailView.as_view()),

]