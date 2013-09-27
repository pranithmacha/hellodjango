
# Create your views here.
from django.shortcuts import render_to_response,HttpResponse
from django.shortcuts import render
from validations import Validations
import requests
from django.utils import simplejson
import AppClientConstants
from django.template import RequestContext
import json
from MyForms import ContactForm


def home(request):
    return render_to_response("myhomepage.html")

def nike(request):
    """
method to return the home page
"""
    return render_to_response('nikeapp.html')
    
def contact(request):
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