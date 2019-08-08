from django.shortcuts import render

from .models import Projects

def show_site(request):
    projects = Projects.objects.all()

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects)
    }

    print('here we go', round(12/len(projects)))

    return render(request, 'intro.html', context)
