from django.contrib import admin

from .models import Post

# and a new admin registration
admin.site.register(Post)
