from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from post import views
from post.views import PostViewSet
from post.views import ShowNotifications

router = DefaultRouter()
router.register('posts', PostViewSet)
# router.register('directors', DirectorView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('notify/', ShowNotifications, name='show-notify')
]