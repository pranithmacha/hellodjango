# Create your views here.
from django.shortcuts import (render_to_response,HttpResponse,render)
import AppClientConstants
from django.template import RequestContext
from models import MyProjects


def home(request):
    return render_to_response("myhomepage.html")

def contact(request):
    return render_to_response("contact.html")
    
def about_me(request):
    return render_to_response("about.html")
    
def projects(request):
    posts = MyProjects.objects.all()
    return render_to_response("projects.html",{"posts":posts})    
    
