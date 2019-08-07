from django.shortcuts import render

# Create your views here.

def show_intro(request):
    return render(request, 'intro.html')
