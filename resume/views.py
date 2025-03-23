from django.shortcuts import render

def home(request):
    # Later, you can pass dynamic data for Alex's portfolio
    return render(request, 'home.html')
