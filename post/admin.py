from django.contrib import admin

from django.contrib import admin
from post.models import *
from embed_video.admin import AdminVideoMixin


class PostImageInline(admin.TabularInline):
    model = PostImage
    max_num = 10
    min_num = 1


@admin.register(Post)
class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    inlines = [PostImageInline]


# class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
#     pass


# admin.site.register(AdminVideo)
admin.site.register(Like)
