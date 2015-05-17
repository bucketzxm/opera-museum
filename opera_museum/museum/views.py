from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext
from django.template.loader import get_template
from opera_museum.settings import BASE_DIR


def index(request):
    print BASE_DIR
    t = get_template("index.html")
    return render_to_response("index.html")



