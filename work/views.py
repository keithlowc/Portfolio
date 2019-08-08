from django.shortcuts import render

from .models import Projects
from .forms import AddContactsForm

def show_site(request):
    projects = Projects.objects.all()

    form = AddContactsForm()

    context = {
        'portfolio': projects,
        'portfolio_size': len(projects),
        'form': form
    }

    print('here we go', round(12/len(projects)))

    return render(request, 'intro.html', context)
