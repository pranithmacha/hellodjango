# Create your views here.

from django.shortcuts import render_to_response,HttpResponse
from mywebsite.validations import Validations
import requests
from django.utils import simplejson
from mywebsite import AppClientConstants
from django.template import RequestContext
import json
from models import posts

validation = Validations()

def create_user(request):
    return render_to_response('CreateUser.html',{},context_instance=RequestContext(request))
    

def nike_create_user(request):
    """
    method to create a user
    """
    print request
    name = request.POST['userName']
    uId = request.POST['userId']
    if validation.check_valid_userName(name):
        userName = name
    else:
        error = AppClientConstants.VALID_NAME
        return render_to_response('CreateUser.html',{'error':error})
    if validation.check_valid_userId(uId):
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
        return render_to_response('result.html',{'message':message,'messageType':message_type,'status':'failure'},context_instance=RequestContext(request))
    else:
        data = result['data']
        name = data['name']
        userId = result['id']
        print data,name,userId
        blogPostData = posts(data=data,name=name,userId=userId)
        blogPostData.save()
        return render_to_response('result.html',{'name':name,'userId':userId,'status':'success'},context_instance=RequestContext(request))


def todo(request):
    return render_to_response('CreateTodo.html',{},context_instance=RequestContext(request))


def createtodo(request):
    userId = request.POST['userId']
    return render_to_response('ResultTodo.html',{"userId":userId})

def list_todos():
    pass



def nike(request):
    """
    #function to render the nikeapp page
    """
    return render_to_response('nikeapp.html')
    
def contact(request):
    """
    #function to render Contact form. 
    #@renders an empty form if get request is made
    #@renders form with errors is form is not valid
   # @renders result page if no errors are found
    """
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return render_to_response('result.html',{'message':'thank you for posting'})
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })

def do_not_delete():
    user_dictionary = {"userName":"kennedy","id":"123"}
    data = simplejson.dumps(user_dictionary)
    return HttpResponse(data,mimetype='application/json')

