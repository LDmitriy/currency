from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello Django World!')
print('test')
# Create your views here.