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

    return render(request, 'intro.html', context)