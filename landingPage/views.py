from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def index(request):
    # return HttpResponse(landing page template)
    return render(request, "index.html")