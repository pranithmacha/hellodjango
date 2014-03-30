# Create your views here.
from django.shortcuts import (render_to_response,HttpResponse,render)
import AppClientConstants
from django.template import RequestContext
from MyForms import ContactForm
from models import MyProjects
from django.core.mail import send_mail, BadHeaderError
import pytumblr
import requests






def home(request):
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
    API_KEY = 'zkZFT9i4OcAGcX158CWtJWPFgArki4mldNqzUkmnHI6FnUmwId'
    url = "http://api.tumblr.com/v2/blog/pranithmacha.tumblr.com/posts/text?api_key="+API_KEY
    
    json_response = requests.get(url).json()
    
    # get the posts with metadata
    # extract out the 
    res = []
    for key in json_response:
        if 'response' in key:
            res = json_response[key]
            
    #print(str(type(res)))'
    my_blogs = []
    for k in res:
        if 'posts' in k:
            my_blogs = res[k]
            
    # 
    #print(type(posts))
    actual_posts = []
    for blog in my_blogs:
        blog_dict = {}
        #content = post['body'].encode('ascii', 'xmlcharrefreplace')
        #title = post['title'].encode('ascii', 'xmlcharrefreplace')

        content = blog['body']
        title = blog['title']
        blog_dict['title'] = title
        blog_dict['content'] = content
        actual_posts.append(blog_dict)
    
    #client = pytumblr.TumblrRestClient('zkZFT9i4OcAGcX158CWtJWPFgArki4mldNqzUkmnHI6FnUmwId')

    # Make the request
    #info = client.blog_info('pranithmacha')
    # Authenticate via API Key
    #client = pytumblr.TumblrRestClient('zkZFT9i4OcAGcX158CWtJWPFgArki4mldNqzUkmnHI6FnUmwId')

    # Make the request
    #posts = client.posts('pranithmacha.tumblr.com')
    return render_to_response("blog.html",{"posts":actual_posts})
    
def projects(request):
    posts = MyProjects.objects.all()
    return render_to_response("projects.html",{"posts":posts})    
    
