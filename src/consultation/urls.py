from django.urls import path
from . import views

app_name = 'consultation'

urlpatterns = [
    path('services/',views.service,name='service'),
    path('connect/', views.connect, name='connect'),
]