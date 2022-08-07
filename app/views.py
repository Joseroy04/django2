from urllib import request
from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1> hello Home </h1>")
def home2(request):
    homepage='homepage.html'
    return render(request,homepage,{})