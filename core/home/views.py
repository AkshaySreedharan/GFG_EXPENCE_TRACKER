from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request): 
    return HttpResponse("hi from the django server....|this is the about page")

def dynamic_url(request,id):
    print("this the value we got in fun =>{id}")
    return render(request,'dynamic_url.html')
    