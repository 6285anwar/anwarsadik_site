from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.

admin.site.register(Blogs)
admin.site.register(Post)
admin.site.register(Projects)


