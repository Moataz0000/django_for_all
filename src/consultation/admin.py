from django.contrib import admin
from .models import Service, Connect
from unfold.admin import ModelAdmin



@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    pass


@admin.register(Connect)
class ConnectAdminc(ModelAdmin):
    pass