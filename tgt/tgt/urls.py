from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tgt.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^TGTapp/', include('TGTapp.urls')),
=======
    #this designates base url for TGTapp
    url(r'^$', include('TGTapp.urls')),
>>>>>>> ea51b6e5271b05a4e2b124379b23d573ccb244f1
)
