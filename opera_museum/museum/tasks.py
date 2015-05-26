from celery import task
from museum.models import Entry

# how to run it?
# python manage.py runserver
# python manage.py celery worker --loglevel=info

@task
def add(x, y):
    return x + y

@task
def add_related_entries(me):
    entry_list = Entry.objects.all()
    for entry in entry_list:
        if entry.name in me.content:
            print(entry.name)
            me.relate_entry.add(entry)
            me.save()
        if me.name in entry.content:
            entry.relate_entry.add(me)
            entry.save()

@task
def delete_relate_entries(me):
    relate_entry_list = me.relate_entry.all()
    for entry in relate_entry_list:
        entry.relate_entry.remove(me)
        entry.save()