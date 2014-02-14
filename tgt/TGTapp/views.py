from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD

def index(request):
    return HttpResponse("Rango says hello world!")
=======
from django.template import RequestContext

# Create your views here.
#This is designates the url for the base TGT app
def index(request):
    return render(request, 'TGTapp/index.html')
>>>>>>> ea51b6e5271b05a4e2b124379b23d573ccb244f1
