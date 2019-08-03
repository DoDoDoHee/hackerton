from django.shortcuts import render

def index(request):
    return render(request, 'light_main.html')

def oneselection(request):
    return render(request, 'one_selection.html')