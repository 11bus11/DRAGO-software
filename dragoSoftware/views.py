from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Services
# Create your views here.


def services(request):
    """ See all services available """
    services = Services.objects.all()

    template = "dragoSoftware/services.html"
    context = {
        'services': services,
    }

    return render(request, template, context)


def home(request):
    """ See all services available """
    services = Services.objects.all()

    template = "dragoSoftware/index.html"
    context = {
        'services': services,
    }

    return render(request, template, context)


def about(request):
    """ See all services available """
    services = Services.objects.all()

    template = "dragoSoftware/about-us.html"
    context = {
        'services': services,
    }

    return render(request, template, context)
