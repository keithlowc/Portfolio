from django.shortcuts import render
from background_task import background

from .models import Projects
from .forms import AddContactsForm

import requests


def show_site(request):
    projects = Projects.objects.all()

    form = AddContactsForm()

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects),
        'form': form
    }

    for project in projects:
        wake_apps(project.project_url)

    return render(request, 'intro.html', context)

@background(schedule=1)
def wake_apps(url):
    requests.get(url)
