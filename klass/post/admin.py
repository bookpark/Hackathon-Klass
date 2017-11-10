from django.contrib import admin

from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
