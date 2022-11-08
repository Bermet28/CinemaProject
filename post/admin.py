from django.contrib import admin

from django.contrib import admin
from post.models import *
from embed_video.admin import AdminVideoMixin


# class PostImageInline(admin.TabularInline):
#     model = PostImage
#     max_num = 10
#     min_num = 1


@admin.register(Post)
class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


# class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
#     pass


# admin.site.register(AdminVideo)
admin.site.register(Like)
admin.site.register(Director)
# admin.site.register(Post)
admin.site.register(Notification)
# admin.site.register(PostImage)
