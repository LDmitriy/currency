from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ContactUs, Rate, Source

from .forms import SourceForm


def contactus(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus.html', context={'contacts': contacts})


def index(request):
    return render(request, 'index.html')


def rates(request):
    rate = Rate.objects.all()
    return render(request, 'rates.html', context={'rates': rate})


def source(request):
    sour = Source.objects.all().order_by('-id')
    return render(request, 'source.html', context={'sour': sour})


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Source/')
    else:
        form = SourceForm()
    return render(request, 'source_create.html', context={'form': form})


def source_update(request, pk):
    instance = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Source/')
    else:
        form = SourceForm(instance=instance)
    return render(request, 'source_update.html', context={'form': form})


def source_delete(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect('/Source/')
    else:
        return render(request, 'source_delete.html', context={'form': instance})
