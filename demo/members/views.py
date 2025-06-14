from django.shortcuts import render
from members.models import member
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def show_memebers(request):
    all_members = member.objects.all()
    template = loader.get_template("members.html")
    context = {
        'all_members': all_members,
    }
    return HttpResponse(template.render(context,request))

def member_detail(request,id):
    req_member = member.objects.get(id=id)
    template = loader.get_template("member_detail.html")
    context = {
        "member":req_member
    }
    return HttpResponse(template.render(context,request))
