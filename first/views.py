from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader,Context
def index(request):
    t=loader.get_template("index.html")
    c=Context({"title":"django","name":"tom"})
    return HttpResponse (t.render(c))