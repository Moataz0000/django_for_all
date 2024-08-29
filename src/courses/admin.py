from django.contrib import admin
from .models import Course
from unfold.admin import ModelAdmin





@admin.register(Course)
class CourseAdmin(ModelAdmin):
    readonly_fields = ['slug']