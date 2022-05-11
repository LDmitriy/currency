from django.core.mail import send_mail
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import ContactUs, Rate, Source
from .forms import SourceForm, ContactUsForm
from django.conf import settings


class SourceList(ListView):
    queryset = Source.objects.all().order_by('-id')
    template_name = 'source.html'


class SourceCreate(CreateView):
    model = Source
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source')


class SourceUpdate(UpdateView):
    model = Source
    template_name = 'source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source')


class SourceDelete(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source')


class ContactUsList(ListView):
    queryset = ContactUs.objects.all().order_by('-id')
    template_name = 'contactus.html'


class ContactUsCreate(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contact_us')

    def _send_email(self):
        recipient = settings.EMAIL_HOST_USER
        subject = 'New user.'
        body = f'''
                Email to reply: {self.object.email_from}
                Subject: {self.object.subject}
                '''

        send_mail(
            subject,
            body,
            recipient,
            ['misfits.mails@gmail.com'],
            fail_silently=False
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


class RatesList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rates.html'
