from django.contrib import admin

from bloggin.models import Post

# and a new admin registration
admin.site.register(Post)