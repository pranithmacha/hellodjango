
# Create your views here.
from django.shortcuts import render_to_response,HttpResponse
from validations import Validations
import requests
from django.utils import simplejson
import AppClientConstants
from django.template import RequestContext
import json




# object for Validations class in validations module
validation = Validations()

def home(request):
    return render_to_response("myhomepage.html")

def nike(request):
    """
method to return the home page
"""
    return render_to_response('CreateUser.html',context_instance=RequestContext(request))

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
        return render_to_response('result.html',{'message':message,'messageType':message_type})
    else:
        data = result['data']
        name = data['name']
        userId = result['id']
        return render_to_response('user_result.html',{'name':name,'userId':userId})

def todo(request):
    return render_to_response('CreateTodo.html',{},context_instance=RequestContext(request))


def createtodo(request):
    userId = request.POST['userId']
    return render_to_response('ResultTodo.html',{"userId":userId})

def list_todos():
    pass


def do_not_delete():
    user_dictionary = {"userName":"kennedy","id":"123"}
    data = simplejson.dumps(user_dictionary)
    return HttpResponse(data,mimetype='application/json')