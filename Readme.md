Follow this tutorial

https://www.merixstudio.com/blog/deploying-docker-heroku-tutorial/

Run the following command to re create a secret key

docker exec <CONTAINER NAME> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Once you have created the application make sure to set the environment variables

heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='<SECRET KEY FROM ABOVE>'


docker exec portfolio_main python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


For deployment ---


heroku create app <App name> --manifest
heroku stack:set container
heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='3we10(9p*j(qbcnqwa=@r%yr8ujjjdx^7w((3^fmalxlrl@pq8'