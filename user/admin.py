from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Tags)
admin.site.register(Story)
admin.site.register(PostStatus)
admin.site.register(PostImage)