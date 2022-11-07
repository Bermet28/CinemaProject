from django.urls import path

from views import *

urlpatterns = [
    path('posts/', PostViewSet.as_view()),
    path('filters/', FilterView.as_view(), name='filter')

]
