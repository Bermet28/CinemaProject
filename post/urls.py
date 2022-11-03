from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from post import views
from post.views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]