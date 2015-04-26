# Create your views here.
from django.shortcuts import (render_to_response, HttpResponse, render)
from MyForms import ContactForm
from models import MyProjects
from django.core.mail import send_mail, BadHeaderError
import logging
import pytumblr
import requests

logger = logging.getLogger(__name__)
global blog_posts
#blog_posts = []
API_KEY = 'zkZFT9i4OcAGcX158CWtJWPFgArki4mldNqzUkmnHI6FnUmwId'
URL = "http://api.tumblr.com/v2/blog/pranithmacha.tumblr.com/posts?"


def mywebsite_logger(f):
    def logger_func(request):
        logger.info(' starting %s' % f.__name__)
        return f(request)
    logger.info(' ending %s' % f.__name__)
    return logger_func


@mywebsite_logger
def home(request):
    #python_posts = tumblr_client().tagged('python')
    #blog_posts.extend(tumblr_client().posts('pranithmacha.tumblr.com')['posts'])
    #blog_posts.extend(tumblr_client().tagged('django')['posts'])
    return render_to_response("myhomepage.html")


def contact(request):
    if request.method == 'POST':
        # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
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
            return render_to_response('result.html', {'message': 'thank you for posting'})
    else:
        form = ContactForm()  # An unbound form
    return render(request, 'contact.html', {'form': form})


def about_me(request):
    return render_to_response("about.html")


def blog_main(request):
    logger.info("rendering the main blog page")
    return render_to_response("blog_main.html")


def blog(request):
    try:
        payload = {'api_key': API_KEY, 'tag': 'pythondjango'}
        response = requests.get(URL, params=payload).json()
    except Exception as err:
        print(err)
    #requests.get()
    #blog_posts.extend(tumblr_client().tagged('django')['posts'])
    #blog_posts = tumblr_client().tagged('django')
    my_posts = []
    for post in blog_posts:
        try:
            my_post = {'title': str(post['title']), 'url': post['post_url']}
            my_posts.append(my_post)
        except Exception as e:
            logger.info(e)
            pass
    t = {}
    t.g
    return render_to_response("blog.html", {"my_posts": my_posts})


def blogname(name):
    print("the name sent is", name)


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
