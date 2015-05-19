from __future__ import print_function
import sys

from django.shortcuts import render, render_to_response, HttpResponse, redirect, RequestContext
from django.template import loader

def index(request):        
    # template = loader.get_template("index.html")
    # context = {"title": "Home"}
    # return render(request, template)
    return render_to_response("index.html")
