# from django.db import models
#
# from django.contrib.auth import get_user_model
# from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.db import models

from account.models import CustomUser
from embed_video.fields import EmbedVideoField

from category.models import Category, Genre

# from rating.models import Rating

User = get_user_model()


class Director(models.Model):
    name = models.CharField('name', max_length=100)
    description = models.TextField('description', blank=True)
    image = models.ImageField('image', upload_to='directors/')

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='posts')
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, related_name='genres', blank=True)
    title = models.CharField(max_length=50, unique=True)
    director = models.ManyToManyField(Director, blank=True)
    description = models.TextField()
    video = EmbedVideoField(null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('poster', upload_to='movies/')

    class Meta:
        ordering = ['-created_ad']

    def __str__(self):
        return f'title: {self.title} {self.category} '


# class PostImage(models.Model):
#     image = models.ImageField(upload_to='media/posts/', blank=True, null=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['post', 'owner']

    def __str__(self):
        return f'{self.post} -> {self.owner}'
