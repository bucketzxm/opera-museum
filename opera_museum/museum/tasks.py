from celery import task


# how to run it?
# python manage.py runserver
# python manage.py celery worker --loglevel=info

@task
def add(x,y):
    return x+y


