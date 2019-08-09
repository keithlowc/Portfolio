from django.shortcuts import render

from .models import Projects
from .forms import AddContactsForm
from portfolio.background_tasks.background import wake_apps, say_something

from portfolio.worker import conn  # background
from rq import Queue  # background

import time

def show_site(request):
    q = Queue(connection=conn)

    projects = Projects.objects.all()
    form = AddContactsForm()

    job = q.enqueue(wake_apps, projects)  # background

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects),
        'form': form,
    }
    time.sleep(5)
    print('results ', job.result)

    return render(request, 'intro.html', context)
