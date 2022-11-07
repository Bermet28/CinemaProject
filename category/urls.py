from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import CategoryViewSet, GenreViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:pk>/', include(router.urls)),
    path('', include(router.urls)),
    path('/<int:pk>/', include(router.urls)),
]
