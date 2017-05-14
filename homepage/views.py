from django.shortcuts import render

def index(request):
    """Homepage"""
    return render(request, 'homepage/index.html')

def about(request):
    """About Section"""
    return render(request, 'homepage/about.html')
