from django.shortcuts import render

from coffees.models import Product
from client.models import Client


def home(request):
    product_obj = Product.objects.all()
    clients_obj = Client.objects.all()

    context = {
        'products': product_obj,
        'clients': clients_obj,
    }
    return render(request, 'home.html', context)
