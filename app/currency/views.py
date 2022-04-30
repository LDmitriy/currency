from django.shortcuts import render

from currency.models import ContactUs, Rate, Source

from currency.forms import SourceForm


def contactus(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus.html', context={'contacts': contacts})


def index(request):
    return render(request, 'index.html')


def rates(request):
    rate = Rate.objects.all()
    return render(request, 'rates.html', context={'rates': rate})


def source(request):
    sour = Source.objects.all()
    return render(request, 'source.html', context={'sour': sour})


def source_create(request):
    sourc = SourceForm()
    return render(request, 'source_create.html', context={'sourc': sourc})
