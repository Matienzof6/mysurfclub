from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q 
# Create your views here.


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())