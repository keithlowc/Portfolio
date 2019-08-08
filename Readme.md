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

#### Once you have created the application make sure to set the environment variables - For security purposes only

```
heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='<SECRET KEY FROM ABOVE>'
```

To Do:

https://trello.com/b/GyVWmKdt/keiths-portfolio


### Resources

https://www.merixstudio.com/blog/deploying-docker-heroku-tutorial/