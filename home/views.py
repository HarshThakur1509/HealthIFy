from dataclasses import field
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from home.models import Doctors, History
from .forms import HistoryForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from home.models import Doctors 



def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    
    return render(request, 'index.html')

def doctor(request):
    if request.method == "POST":
        query = request.POST['query']
        ser = (Q(name__icontains = query) | Q(specialzation__icontains = query) | Q(fees__icontains = query))
        doc = Doctors.objects.filter(ser)
        return render(request, 'doctor.html', {'doc': doc})
    else:
        doc = Doctors.objects.all()
        return render(request, 'doctor.html', {'doc': doc})


def history(request):
    
    his = History.objects.get(user = request.user)
    form = HistoryForm(request.POST or None, instance=his)
    if request.method == "POST":
        
        
        if form.is_valid():
            
            form.save()
            
            return redirect('/')
    
   
    return render(request, 'history.html', {'form': form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")
        
    return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/index')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form':form,})