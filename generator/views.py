# Step 3: Creating the views pointing to the templates (templates/<appname>) and passing necessary info.
# Step 4: Creating the html files in templates/<appname> 
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
    
def password(request):
    generatedPassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('specialCharacters'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length'))

    for x in range(length):
        generatedPassword += random.choice(characters)

    return render(request, 'generator/password.html', { 'password': generatedPassword })

def about(request):
    return render(request, 'generator/about.html')