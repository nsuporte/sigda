from django.shortcuts import render

# Create your views here.

def registarse(request):
    return render(request, 'conta/registarse.html')