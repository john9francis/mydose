from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('doctor_portal/index.html')
    return HttpResponse(template.render())

def LoginView(request):
    return HttpResponse("Login:")