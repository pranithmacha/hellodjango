
# Create your views here.
from django.shortcuts import render_to_response,HttpResponse
from validations import Validations
import requests
from django.utils import simplejson
import AppClientConstants
from django.template import RequestContext
import json


def home(request):
    return render_to_response("myhomepage.html")

def nike(request):
    """
method to return the home page
"""
    return render_to_response('nikeapp.html')

def do_not_delete():
    user_dictionary = {"userName":"kennedy","id":"123"}
    data = simplejson.dumps(user_dictionary)
    return HttpResponse(data,mimetype='application/json')