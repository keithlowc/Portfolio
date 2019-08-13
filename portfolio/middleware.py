from work.background_jobs import background_functions
from work.models import Projects

import asyncio
import requests


'''
This middleware function checks if an user has opened the website and sends a signal
to AsyncIO to wake up the apps on the portfolio by sending a GET
request to them in a Asynchronous manner. Usually takes 30 seconds to wake an app. This helps to preload them.
'''
class WakeAppsOnUserVisit:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        urls_list = []
        is_home = request.path_info.startswith('')

        if is_home:
            projects = Projects.objects.all()

            for project in projects:
                urls_list.append(project.project_url)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_in_executor(None, wake_apps, urls_list)
            
        return self.get_response(request)


def wake_apps(urls_list):
    for url in urls_list:
        requests.get(url)
        print('Sending requests - for: ', url)

