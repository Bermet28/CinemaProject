from django.contrib.auth import get_user_model
from django.db import models

from category.models import Category
from account.models import CustomUser


# User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='posts')
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_ad = models.DateTimeField()
    image = models.ImageField(upload_to='gallery')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'title: {self.title} {self.description} '


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
