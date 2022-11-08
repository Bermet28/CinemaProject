from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from django.db import models
from account.models import CustomUser
from embed_video.fields import EmbedVideoField
from category.models import Category, Genre

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


class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'like'), (2, 'Comment'), (3, 'Follow'))
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='noti_post', blank=True, null=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='noti_from_user', null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='noti_to_user', null=True)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES, null=True)
    text_preview = models.CharField(max_length=90, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    class Meta:
        unique_together = ['post', 'owner']

    def __str__(self):
        return f'{self.post} -> {self.owner}'

    def user_liked_posts(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.owner

        notify = Notification(post=post, sender=sender, user=post.owner, notification_type=1)
        notify.save()

    def user_unlike_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.owner
        notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
        notify.delete()


post_save.connect(Like.user_liked_posts, sender=Like)
post_delete.connect(Like.user_unlike_post, sender=Like)

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
#
#     class Meta:
#         unique_together = ['post', 'owner']
#
#     def __str__(self):
#         return f'{self.post} -> {self.owner}'
