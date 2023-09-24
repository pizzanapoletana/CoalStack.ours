from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'coalstack/homepage.html')

def history(request):
    return render(request, 'coalstack/chathistory.html')
    
def login(request):
    return render(request, 'coalstack/login.html')

def landing(request):
    return render(request, 'coalstack/landing.html')