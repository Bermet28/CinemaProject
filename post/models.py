# from django.contrib.auth import get_user_model
# from django.core.validators import FileExtensionValidator
from django.db import models


from category.models import Category
from account.models import CustomUser
from embed_video.fields import EmbedVideoField


# User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='posts', null=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    video = EmbedVideoField(null=True)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_ad']

    def __str__(self):
        return f'title: {self.title} {self.category} '


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


