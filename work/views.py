from django.shortcuts import render
from background_task import background
from django.contrib import messages
from django.shortcuts import redirect

from .models import Projects
from .forms import AddContactsForm

import requests


def show_site(request):
    projects = Projects.objects.all()

    form = AddContactsForm()

    if request.method == 'POST':
        form = AddContactsForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Succesfully added comment')
        else:
            messages.warning(request, 'Something went wrong! Please check your comment')
    
    form = AddContactsForm()

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects),
        'form': form
    }

    return render(request, 'intro.html', context)
