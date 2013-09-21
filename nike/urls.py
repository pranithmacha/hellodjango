from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^create_user', 'views.create_user', name='create-user'),
    url(r'^todo', 'views.todo', name='to-do'),
    url(r'^create_todo', 'views.createtodo', name='create-a-to-do'),
       
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    """
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/hellodjango/hellodjango/templates/'}),
    """
)
