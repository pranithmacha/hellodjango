# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response,HttpResponse
from mywebsite import validations.Validations
import requests
from django.utils import simplejson
from mywebsite import AppClientConstants
from django.template import RequestContext
import json

validation = Validations()

def create_user(request):
    """
method to create a user
"""
    name = request.POST['userName']
    uId = request.POST['userId']
    if validation.check_valid_userName(name) == True:
        userName = name
    else:
        error = AppClientConstants.VALID_NAME
        return render_to_response('CreateUser.html',{'error':error})
    if validation.check_valid_userId(uId) == True:
        userId = uId
    else:
        error = AppClientConstants.VALID_USER_ID
        return render_to_response('CreateUser.html',{'error':error})
    payload = {"name":userName,"id":userId}
    url = "http://nike-todo.aws.af.cm/users/"
    result = requests.post(url, data=payload).json()
   
    if 'message' in result:
        message = result['message']
        message_type =result['messageType']
        return render_to_response('result.html',{'message':message,'messageType':message_type,'status':'failure'})
    else:
        data = result['data']
        name = data['name']
        userId = result['id']
        return render_to_response('result.html',{'name':name,'userId':userId,'status':'success'})

def todo(request):
    return render_to_response('CreateTodo.html',{},context_instance=RequestContext(request))


def createtodo(request):
    userId = request.POST['userId']
    return render_to_response('ResultTodo.html',{"userId":userId})

def list_todos():
    pass
