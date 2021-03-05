from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def subscribe(request):
  # function take email adress and  submitts it to mailchimp
  '''
  take email adress as input to subscribe/
  checks to see if email exist
    if exist
      say "ydou have already subscribed
    else if
      subscribe to mailchip
  '''
  pass