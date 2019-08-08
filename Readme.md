Keith's personal portfolio website. The website itself is a Django application hosted on heroku. Since most of my projects are hosted for free on heroku the servers go to sleep every 30 seconds. So, when someone opens this website, it becomes a gateway to waking up the other websites via a GET request that run on the background. Also, this website is built as a Content Management System - Thus, I am able to change most of the things on the website without pushing new code.

### Run the following command to re-create a secret key

```
docker exec <CONTAINER NAME> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Instructions to deploy app to heroku servers with heroku.yml

```
heroku create app <App name> --manifest
heroku stack:set container

git init
git add .
git commit -m "<message here>"
git push heroku master
```

### Once you have created the application make sure to set the environment variables - For security purposes only

```
heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='<SECRET KEY FROM ABOVE>'
```

### To Do:

https://trello.com/b/GyVWmKdt/keiths-portfolio


### Resources

https://www.merixstudio.com/blog/deploying-docker-heroku-tutorial/