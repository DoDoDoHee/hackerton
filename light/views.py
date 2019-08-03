from django.shortcuts import render

def index(request):
    return render(request, 'light_main.html')