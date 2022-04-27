from django.shortcuts import render

from currency.models import ContactUs, Rate


def contactus(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus.html', context={'contacts': contacts})


def index(request):
    return render(request, 'index.html')


def rates(request):
    rate = Rate.objects.all()
    return render(request, 'rates.html', context={'rates': rate})
