#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render


def func(request):
    return HttpResponse("This is my first django project!")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    str = u"Welcome to Django Project!!!"
    return render(request, 'home.html', {'string': str})
