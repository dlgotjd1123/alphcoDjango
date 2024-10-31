from django.contrib import admin
# from .models import Posts
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created", "updated"]
# admin.site.register(Posts, PostAdmin)
admin.site.register(Notice)
