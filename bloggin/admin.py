from django.contrib import admin
from .models import Post, Category

# and a new admin registration
admin.site.register(Post)
admin.site.register(Category)
