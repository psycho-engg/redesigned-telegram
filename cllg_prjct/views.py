from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    msg = 'Login Successfully'
    return render(request,'home.html',{'m':msg})

def python(request):
    return render(request,'python.html')

def login(request):
    return render(request,'login.html')

def c(request):
    return render(request,'c.html')

def thanx(request):
    article = request.GET['article']
    topic_name = request.GET['topic_name']
    return render(request,'thanx.html',{'article':article,'topic_name':topic_name})
