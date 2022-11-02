from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


