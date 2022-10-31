from django.contrib import admin
from django.contrib.admin import site

from category.models import Category

site.admin.register(Category)
