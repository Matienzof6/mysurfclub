from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.



def hostel(request):
    template = loader.get_template('hostel.html')
    return HttpResponse(template.render())


