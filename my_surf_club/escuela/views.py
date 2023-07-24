from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def escuela(request):
    template = loader.get_template('escuela.html')
    return HttpResponse(template.render())