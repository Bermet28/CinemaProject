from django.contrib.auth import get_user_model
from django.db import models

from account.models import CustomUser
from post.models import Post

User = get_user_model()


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    movie = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.movie} -> {self.created_at}'


class Favorites(models.Model):
    movie = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['movie', 'owner']
