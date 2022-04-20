from django.http import HttpResponse

from currency.models import ContactUs


def contactus(request):
    li = []
    for contact in ContactUs.objects.all():
        li.append((contact.id, contact.email_from, contact.subject, contact.message))
    return HttpResponse(str(li))
