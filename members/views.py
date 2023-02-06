from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
    
def register_user(request):
    form = UserCreationForm()
    return render(request, 'frontend/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')
            return redirect('login_user')
    else:
        return render(request, 'members/login.html')