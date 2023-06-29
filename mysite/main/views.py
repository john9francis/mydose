from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def patient_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('patient_portal'))
    else:
        form = AuthenticationForm()

    return render(request, 'main/patient_login.html', {'form': form})


def patient_portal(request):
    '''includes a link to the patient portal'''
    return render(request, 'main/patient_portal.html')


def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('doctor_portal'))
    else:
        form = AuthenticationForm()

    return render(request, 'main/doctor_login.html', {'form': form})

def doctor_portal(request):
    '''includes a link to the doctor portal'''
    return render(request, 'main/doctor_portal.html')
