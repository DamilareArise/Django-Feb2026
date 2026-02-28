from django.contrib import admin
from .models import Category, UserPost

# Register your models here.
admin.site.register(Category)
admin.site.register(UserPost)