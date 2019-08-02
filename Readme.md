Follow this tutorial

https://www.merixstudio.com/blog/deploying-docker-heroku-tutorial/

Run the following command to re create a secret key

docker exec <CONTAINER NAME> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


Once you have created the application make sure to set the environment variables

heroku config:set DEBUG=False ALLOWED_HOSTS='*'



