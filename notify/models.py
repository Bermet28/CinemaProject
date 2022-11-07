from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from account.models import CustomUser
from post.models import Post


class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'like'), (2, 'Comment'), (3, 'Follow'))
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='noti_post', blank=True, null=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='noti_from_user', null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='noti_to_user', null=True)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES, null=True)
    text_preview = models.CharField(max_length=90, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)


class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    def user_liked_posts(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user

        notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
        notify.save()

    def user_unlike_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
        notify.delete()


post_save.connect(Likes.user_liked_posts, sender=Likes)
post_delete.connect(Likes.user_unlike_post, sender=Likes)

