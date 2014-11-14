from django.conf.urls import (patterns, include, url)
from mywebsite import views
import settings
from django.contrib import admin


BASE_DIR = settings.BASE_DIR
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/',include(admin.site.urls)),
    url(r'^500/$', 'mywebsite.views.error500_handler',name='error_page'),
    url(r'^404/$', 'mywebsite.views.error404_handler',name='error_page'),
    url(r'^$', 'mywebsite.views.home', name=''),
    url(r'^home$', 'mywebsite.views.home', name=''),
    url(r'^projects$', 'mywebsite.views.projects', name='projects'),
    url(r'^about$', 'mywebsite.views.about_me', name='about me'),
    url(r'^contact$', 'mywebsite.views.contact', name='contact'), 
    url(r'^blog$', 'mywebsite.views.blog', name='contact'), 
    url(r'^contact/*$', 'mywebsite.views.contact', name='contact'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': BASE_DIR+'/templates/'}),
    
    # url(r'^physics/*$', 'mywebsite.views.physics', name='physics'), 
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^physics/*$', 'mywebsite.views.physics', name='contact'),      
    
)

