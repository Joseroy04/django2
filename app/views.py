from urllib import request
from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1> hello Home </h1>")

def index(request):
    homepage='templates/allpage/index.html'
    return render(request,homepage,{})

def home2(request):
    homepage='templates/allpage/index.html'
    return render(request,homepage,{})

def medichine(request):
    return render(request,'templates/allpage/medichine.html',{})


def contact(request):
    return render(request,'templates/allpage/contact.html',{})


def health(request):
    return render(request,'templates/allpage/health.html',{})


def news(request):
    return render(request,'templates/allpage/news.html',{})


def client(request):
    return render(request,'templates/allpage/client.html',{})

