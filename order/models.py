from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()


class Mark:
    one = 1
    two = 2
    marks = ((one, 'bought'), (two, 'watch'))


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ManyToManyField(Post, through=OrderItem)
    status = models.PositiveSmallIntegerField(choices=Mark.marks)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} -> {self.user}'
