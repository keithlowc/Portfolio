import requests
 

'''
This function takes a projects object and sends get requests to the 
applications, to wake them up. On start of the portfolio webapp
'''
def wake_apps(projects):
    r = requests.get('https://ecovisorv2.herokuapp.com')
    return r
    # url_list = []

    # for project in projects:
    #     url_list.append(project.project_url)

    # for i, url in enumerate(url_list):
    #     print("The url ", url)
    #     requests.get(url)

def say_something():
    print("Hello world")
    return 1

