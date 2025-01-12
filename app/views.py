from django.shortcuts import render, redirect
from django.contrib.auth.forms import  PasswordChangeForm
from app.forms import UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "user registered successfully")
            return redirect('login')
        else:
            messages.error(request, "Enter details correctly")
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form':form})


def logIn(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          print(username)
          user = authenticate(request, username=username, password=password)
          if user is not None:
            login(request, user)
            return redirect('dashboard')
          else:
              form.add_error(None, "Invalid details")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "password changed successfully")
            return redirect('login')
        else:
            messages.error(request, "enter details correctly")
    else:
        form = PasswordChangeForm(request)
    return render(request, 'changepassword.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html',{'user':request.user})    


@login_required
def profile(request):
    return render(request, 'profile.html', {'user':request.user})

@login_required
def LogOut(request):
    logout(request)
    return redirect('login')