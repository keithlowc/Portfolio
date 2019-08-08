# Run the following command to re-create a secret key

```
docker exec <CONTAINER NAME> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Once you have created the application make sure to set the environment variables - For security purposes only

```
heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='<SECRET KEY FROM ABOVE>'
```

# Instructions to deploy app to heroku servers with heroku.yml

```
heroku create app <App name> --manifest
heroku stack:set container
heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='3we10(9p*j(qbcnqwa=@r%yr8ujjjdx^7w((3^fmalxlrl@pq8'
```

To Do:

# Need to create the models for the portfolios - So if i want to update a new project - i can just add it through the admin

Model portfolio

Takes: 
    title, 
    description, 
    url to the project 
    url of an image

# Need to make a form to take in the people who sign up on my website, and i should also get an email directly to me. Maybe use twilio too 

# Need to make a function to wake up all projects - So that when someone gets inside the website it sends a get request to all projects on heroku
# And wakes them up - by the time the user clicks something - They are ready to go.
# Admin is broken when debug = False - Need to fix this. 


# Resources

https://www.merixstudio.com/blog/deploying-docker-heroku-tutorial/