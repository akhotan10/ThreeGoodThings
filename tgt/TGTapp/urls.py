from django.conf.urls import patterns, url
from TGTapp import views

<<<<<<< HEAD
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
=======
#makes the base index for TGTapp
urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
)
>>>>>>> ea51b6e5271b05a4e2b124379b23d573ccb244f1
