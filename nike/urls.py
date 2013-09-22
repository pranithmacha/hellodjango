from django.conf.urls import patterns, include, url
import views
from hellodjango import settings

BASE_DIR = settings.BASE_DIR

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^create_user', 'nike.views.create_user', name='create-user'),
    url(r'^todos', 'nike.views.todo', name='to-do'),
    url(r'^create_todo', 'nike.views.createtodo', name='create-a-to-do'),
    
    # including the static files
    # BASE_DIR = /hellodjango/hellodjango 
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': BASE_DIR + '/templates/'}),
   
)
