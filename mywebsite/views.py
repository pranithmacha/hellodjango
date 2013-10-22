# Create your views here.
from django.shortcuts import (render_to_response,HttpResponse,render)
import AppClientConstants
from django.template import RequestContext
from MyForms import ContactForm
from models import MyProjects
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render_to_response("myhomepage.html")

def contact(request):
    """
    #function to render Contact form. 
    #@renders an empty form if get request is made
    #@renders form with errors is form is not valid
   # @renders result page if no errors are found
    """
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
             # All validation rules pass
             subject = request.POST.get('subject', '')
             message = request.POST.get('message', '')
             sender = request.POST.get('sender', '')
             if subject and message and sender:
                 try:
                     send_mail(subject, message, sender, ['pranith@machaiswho.im'])
                 except BadHeaderError:
                     return HttpResponse('Invalid header found.')
            return render_to_response('result.html',{'message':'thank you for posting'})
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
    
def about_me(request):
    return render_to_response("about.html")
    
def projects(request):
    posts = MyProjects.objects.all()
    return render_to_response("projects.html",{"posts":posts})    
    
