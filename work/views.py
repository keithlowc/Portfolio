from django.shortcuts import render
from background_task import background
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .models import Projects
from .forms import AddContactsForm

import requests

'''
View created to redirect the user to /home path - Helps with capturing analytics
'''
def redirect_to_site(requests):
    return redirect('show_site')


'''
Main view to show the whole site
'''
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
            messages.warning(request, 'Something went wrong! Please check your form')
    
    form = AddContactsForm()

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects),
        'form': form
    }

    return render(request, 'intro.html', context)


'''
Analytics related routes - We use these to have the middleware run
on these specific routes.
'''
def capture_github(requests):
    print('Works')
    return HttpResponseRedirect('https://github.com/keithlowc')


def capture_linkedin(requests):
    print('Works')
    return HttpResponseRedirect('https://www.linkedin.com/in/keithlowc/')


def capture_instagram(requests):
    print('Works')
    return HttpResponseRedirect('https://instagram.com/keithlwc')

