from django.contrib import admin
from account.models import Spam_Contacts, CustomUser

# # Register your models here.

admin.site.register(Spam_Contacts)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'auth_provider', 'created_at']


admin.site.register(CustomUser)