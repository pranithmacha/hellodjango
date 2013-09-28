
# Create your views here.
from django.shortcuts import (render_to_response,HttpResponse,render)
import AppClientConstants
from django.template import RequestContext
from MyForms import ContactForm


def home(request):
    return render_to_response("myhomepage.html")

def nike(request):
    """
    function to render the nikeapp page
    """
    return render_to_response('nikeapp.html')
    
def contact(request):
    """"
    function to render Contact form. 
    @renders an empty form if get request is made
    @renders form with errors is form is not valid
    @renders result page if no errors are found
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