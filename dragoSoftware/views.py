from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Services, AboutUs
# Create your views here.


def services(request):
    """ See all services available """
    our_services = Services.objects.all()

    template = "dragoSoftware/services.html"
    context = {
        'our_services': our_services,
    }

    return render(request, template, context)


def home(request):
    """ See all services available """
    services = Services.objects.all()
    abouts = AboutUs.objects.all()

    template = "dragoSoftware/index.html"
    context = {
        'services': services,
        'abouts': abouts,
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
