from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('login/index.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login/login.html')
    return HttpResponse(template.render())