from django.contrib import admin
from .models import Post, Comment
from unfold.admin import ModelAdmin


@admin.register(Post)
class  PostAdmin(ModelAdmin):
    list_display = ['title', 'publish' , 'status', 'author']
    list_filter  = ['created', 'status', 'publish']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    readonly_fields = ['slug']




@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']    