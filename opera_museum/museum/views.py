from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext
from django.template.loader import get_template



def index(request):
    t = get_template("index.html")
    return render_to_response("index.html")



