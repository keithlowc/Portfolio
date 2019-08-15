from django.shortcuts import render
from background_task import background
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .models import Projects, PageData
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

    data = 'Value has not been defined!'

    try:
        data = PageData.objects.all()[0]
    except Exception as e:
        print('Error ', e)

    form = AddContactsForm()

    if request.method == 'POST':
        form = AddContactsForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Succesfully submitted message!')
        else:
            messages.warning(request, 'Something went wrong! Please check your form!')
    
    form = AddContactsForm()

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects),
        'data': data,
        'form': form
    }

    return render(request, 'intro.html', context)


'''
Analytics related routes - We use these to have the middleware run
on these specific routes.
'''
def capture_github(requests):
    return HttpResponseRedirect('https://github.com/keithlowc')


def capture_linkedin(requests):
    return HttpResponseRedirect('https://www.linkedin.com/in/keithlowc/')


def capture_instagram(requests):
    return HttpResponseRedirect('https://instagram.com/keithlwc')
