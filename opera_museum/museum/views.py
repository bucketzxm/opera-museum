from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext
from django.template.loader import get_template

from models import Entry, Tag


def index(request):
    t = get_template("index.html")
    return render_to_response("base.html")


def search(request):
    if request.method == "POST":
        key_word = request.POST['key_word']


        #filter entries equals key_words
        entries = Entry.objects.all().filter(name=key_word)

        #filter entries which tags equals to key_words
        tags = Entry.objects.all().filter(key=key_word)
        if not tags:
            for tag in tags:
                entries.extend(Entry.objects.all().filter(tag=tag))


    else:
        return HttpResponse("")