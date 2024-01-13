from django.http import HttpResponse
from django.shortcuts import render
from . models import *


def website(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, 'index.html', {'result': obj, 'member': obj2})





