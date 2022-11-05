# from django.db import models
#
# from django.contrib.auth import get_user_model
# from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.db import models

from account.models import CustomUser
from embed_video.fields import EmbedVideoField

from category.models import Category, Genre

User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='posts')
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, related_name='genres', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, unique=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    video = EmbedVideoField(null=True)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_ad']

    def __str__(self):
        return f'title: {self.title} {self.category} '


class PostImage(models.Model):
    image = models.ImageField(upload_to='media/posts/', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['post', 'owner']

    def __str__(self):
        return f'{self.post} -> {self.owner}'

# class Favorites(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
#     movie =
