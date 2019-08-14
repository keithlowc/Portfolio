from work.models import Projects, Analytics

import asyncio
import requests


'''
This middleware function checks if an user has opened the website 
and sends a signal to AsyncIO to wake up the apps on the portfolio 
by sending a GET request to them in a Asynchronous manner. Usually 
takes 30 seconds to wake an app. This helps to preload them.
'''
class WakeAppsOnUserVisit:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        urls_list = []
        is_home = request.path_info.startswith('/home')

        if is_home:
            projects = Projects.objects.all()
            for project in projects:
                urls_list.append(project.project_url)

        if len(urls_list) > 0:
            # Asynchronous functions
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_in_executor(None, wake_apps, urls_list)
            # Asynchronous functions
        
        return self.get_response(request)

'''
Function created to send a GET request to a list of URLS
'''
def wake_apps(urls_list):
    for url in urls_list:
        requests.get(url)
        print('Sending requests - for: ', url)

'''
Middleware created to capture analytics based on clicks.
'''
class CaptureAnalytics:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        is_github = request.path_info.startswith('/github')
        is_linkedin = request.path_info.startswith('/linkedin')
        is_instagram = request.path_info.startswith('/instagram')

        if is_github:
            git = Analytics(type_of_analytics='G')
            git.save()
        elif is_linkedin:
            linkedin = Analytics(type_of_analytics='L')
            linkedin.save()
        elif is_instagram:
            instagram = Analytics(type_of_analytics='I')
            instagram.save()

        return self.get_response(request)
