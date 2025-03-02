from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q 
# Create your views here.



def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))





def testing(request):
    # mydata = Member.objects.filter(Q(firstname__startswith='M') | Q(firstname__endswith='o')).values()
    mydata = Member.objects.all().order_by('lastname', 'id').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,   
    }
    return HttpResponse(template.render(context, request))