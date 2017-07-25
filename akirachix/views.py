from django.shortcuts import render
from django.http import HttpResponse
from.models import Students
from.models import Teachers




# Create your views here.
#def welcome(request):
    #return HttpResponse("<p>Welcome to Akirachix class</p>")
#def Teachers(request):
    #return HttpResponse("<p>Here we will show all Teachers</p>")
    
def welcome(request):
     return render(request,'index.html')
def students(request):
     return HttpResponse("<p>Here we will show all Students</p>")

    

