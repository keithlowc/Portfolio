import requests

from background_task import background


'''
Sets background job to send a GET request to an url. The function
is scheduled to be run at 1 sec of being called.
'''
@background(schedule=1)
def wake_apps(url):
    try:
        requests.get(url)
        print('Sending request from background')
    except Exception as e:
        print('ERROR: ', e)
    # pass
