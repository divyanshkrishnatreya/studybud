from django.http import HttpResponse
from django.urls import path 
from . import views 

urlpatterns = [
    path()
    
]
def home(request):
    return  HttpResponse("Home Page")
def room(request):
    return HttpResponse("Room")
