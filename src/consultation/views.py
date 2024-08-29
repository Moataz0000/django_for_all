from django.shortcuts import render
from .models import Service, Connect





def service(request):
    service = Service.objects.all()
    return render(request, 'consultation/service.html', {'service':service})




def connect(request):
    connect = Connect.objects.all()
    return render(request, 'consultation/connect.html', {'connect':connect})