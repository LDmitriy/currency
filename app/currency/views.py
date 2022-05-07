from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import ContactUs, Rate, Source
from .forms import SourceForm


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
    queryset = ContactUs.objects.all()
    template_name = 'contactus.html'


class RatesList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rates.html'
