from work.background_jobs import background_functions
from work.models import Projects

import subprocess

'''
This middleware function checks if an user has opened the website and sends a signal
to the django-background-tasks to wake up the apps on the portfolio by sending a GET
request to them. Usually takes 30 seconds to wake an app. This helps to preload them.
'''
class WakeAppsOnUserVisit:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        is_home = request.path_info.startswith('/')

        if is_home:
            projects = Projects.objects.all()

            for project in projects:
                background_functions.wake_apps(project.project_url)
                print('Sending request to background job')
            
        return self.get_response(request)

