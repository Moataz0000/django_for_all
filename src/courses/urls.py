from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('course/', views.list_of_courses, name='list_courses'),

    path('<slug:slug>/', views.course_detail, name='course_detail'),
]