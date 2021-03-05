from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime
from .models import Greeting
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
  "api_key": os.getenv("MAILCHIMP_API_KEY"),
  "server": os.getenv("MAILCHIMP_DATA_CENTER")
})

list_id = os.getenv("MAILCHIMP_EMAIL_LIST_ID")

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def subscribe(request):
  # function take email adress and  submitts it to mailchimp
  if request.method == 'POST':
        email = request.POST['email_id']
        member_info = {

            "email_address": email,
            "status": "subscribed",
        }
        try:
            mailchimp.lists.add_list_member(list_id, member_info)
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))
        html = "<html><body>Thank you for your interest %s.</body></html>" %email
        return HttpResponse(html)