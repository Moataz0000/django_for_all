from django.contrib import admin
from .models import Post
from unfold.admin import ModelAdmin


@admin.register(Post)
class  PostAdmin(ModelAdmin):
    list_display = ['title', 'publish' , 'status', 'author']
    list_filter  = ['created', 'status', 'publish']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    readonly_fields = ['slug']