from django.shortcuts import render

from service.models import Service
from client.models import Client


def home(request):
    services_obj = Service.objects.all()
    clients_obj = Client.objects.all()

    context = {
        'services': services_obj,
        'clients': clients_obj,
    }
    return render(request, 'home.html', context)