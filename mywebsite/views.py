# Create your views here.
from django.shortcuts import (render_to_response,HttpResponse,render)
from django.template import RequestContext
from MyForms import ContactForm
from models import MyProjects
from django.core.mail import send_mail, BadHeaderError
import requests
from hellodjango import AppConsts
import manage
import logging
import pytumblr

logger = logging.getLogger(__name__)


def mywebsite_logger(f):
    def logger_func(request):
        logger.debug(' beginning ')
        return f(request)
        #logger.debug(' ending ')       
    return logger_func


@mywebsite_logger
def home(request):
    logger.debug('this is my new log message !!')
    return render_to_response("myhomepage.html")


def contact(request):
    if request.method == 'POST': 
        # If the form has been submitted...
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
    return render(request, 'contact.html', {'form': form})


def about_me(request):
    return render_to_response("about.html")


def blog(request):
    blog_posts = tumblr_client().posts('pranithmacha.tumblr.com')['posts']
    my_posts = []
    for post in blog_posts:
        try:
            my_post = {}
            my_post['title'] = str(post['title'])
            my_post['url'] = post['post_url']
            my_posts.append(my_post)
        except Exception as e:
            logger.info(e)
            print e
            pass
    return render_to_response("blog.html", {"my_posts": my_posts})


def projects(request):
    posts = MyProjects.objects.all()
    return render_to_response("projects.html", {"posts": posts})


def error500_handler(request):
    return render_to_response("500.html") 


def error404_handler(request):
    return render_to_response("404.html") 


def tumblr_client():
    client = pytumblr.TumblrRestClient(
  'zkZFT9i4OcAGcX158CWtJWPFgArki4mldNqzUkmnHI6FnUmwId',
  'ajdlmAP6EdOZA2J2xkaPE6sOkMuQn80NZft7RoxgCxwcaRcUZk',
  'hpYYBkq4esqAKUgp2A3czNqYIaZG78kUvnhFG9VUNT0EylWedP',
  'LktJK59A7zMHeXdrJ5UZeBgcgkOY7oDCBeKuUk89Y0zjFQgM8W'
   )
    return client

