from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CashBox, FamilyMember, Membership
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm

# Views
def home(request):
    return render(request, 'home.html')

def box_list(request):
    """Displays the list of all CashBoxes."""
    boxes = CashBox.objects.all()
    return render(request, 'box_list.html', {'boxes': boxes})


def box_detail(request, box_id):
    """Displays details of a specific CashBox."""
    box = CashBox.objects.get(id=box_id)
    members = Membership.objects.filter(cash_box=box, cycle=box.current_cycle)
    return render(request, 'lottery/box_detail.html', {
        'box': box,
        'members': members
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
