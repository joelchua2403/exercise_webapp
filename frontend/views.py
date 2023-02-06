from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'frontend/home.html')

def register(request):
    return render(request, 'frontend/register.html')

def login(request):
    return render(request, 'frontend/login.html')

def exercise(request):
    exercises = Exercise.objects.all()
    return render(request, 'frontend/all_exercises.html', {'exercises': exercises})

def about(request):
    return HttpResponse('About page')

def abs(request):
    abs = Exercise.objects.filter(muscle_group__icontains ='ab')
    return render(request, 'frontend/abs.html', {'abs': abs}) 

def chest(request):
    chest = Exercise.objects.filter(muscle_group__icontains ='chest')
    return render(request, 'frontend/chest.html', {'chest': chest})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        exercises = Exercise.objects.filter(exercise__icontains=searched)
        return render(request, 'frontend/search.html', {'searched': searched, 'exercises': exercises})
    else:
        return render(request, 'frontend/search.html', {})
    
