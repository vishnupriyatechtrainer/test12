from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def men(request):
    # return HttpResponse('this is menspage')
    return render(request,'men/men.html')


def watches(request):
    return HttpResponse('this is mens watch')

def shoes(request):
    return HttpResponse('this is mens shoe')