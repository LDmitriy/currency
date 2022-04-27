from django.http import HttpResponse
from django.shortcuts import render

from currency.models import ContactUs, Rate


def contactus(request):
    # li = []
    # for contact in ContactUs.objects.all():
    #     li.append((contact.id, contact.email_from, contact.subject, contact.message))
    # return HttpResponse(str(li))
    contacts = ContactUs.objects.all()
    return render(request, 'contactus.html', context={'contacts': contacts})


def index(request):
    return render(request, 'index.html')


def rates(request):
    rate = Rate.objects.all()
    return render(request, 'rates.html', context={'rates': rate})
