from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from post.views import PostViewSet
from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api/', include(router.urls)),
    path('v1/api/', include('category.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


