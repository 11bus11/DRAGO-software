from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Services, AboutUs
# Create your views here.


def home(request):
    """ See all services available """
    services = Services.objects.all()
    abouts = AboutUs.objects.all()

    ordering = ['nr']

    print(abouts)

    template = "dragoSoftware/index.html"
    context = {
        'services': services,
        'abouts': abouts,
    }

    return render(request, template, context)
