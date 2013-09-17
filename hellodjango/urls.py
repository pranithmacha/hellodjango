from django.conf.urls import patterns, include, url
from mywebsite import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mywebsite.views.home', name='home'),
    url(r'^nike$', 'mywebsite.views.nike', name='nike'),
    url(r'^create_user', 'AppClient.views.create_user', name=''),
    url(r'^todo', 'AppClient.views.todo', name=''),
    url(r'^create_todo', 'AppClient.views.createtodo', name=''),
    
   
    
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'mywebsite/templates/'}),
)
