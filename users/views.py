import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index(request):
    # i = 1/0
    return HttpResponse("hello world")


def say(request):
    return HttpResponse("say")


def sayhello(request):
    return HttpResponse("say hello")


def to_rv(request):
    url_name = reverse('users:reverse')
    return HttpResponse(url_name)


def weather(request, city, time):
    content = city + "  " + time
    return HttpResponse(content)


def t_params(request):
    name = request.GET.get("name")
    age = request.GET.get("age")

    # a = request.POST.get("a")
    # b = request.POST.get("b")

    print(request.GET.getlist)
    content = name + " age is " + age # + " " +a + " " + b
    return HttpResponse(content)
