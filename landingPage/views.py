from django.shortcuts import render
from django.http import HttpRequest
from .models import Signup
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import os

# Global variables
mailchimp_api_key= os.getenv('MAILCHIMP_API_KEY')
mailchimp_server= os.getenv('MAILCHIMP_DATA_CENTER')
mailchimp_list_id= os.getenv('MAILCHIMP_EMAIL_LIST_ID')


# Create your views here.
def index(request):
    # return HttpResponse(landing page template)
    return render(request, "index.html")

def Signup(request):
    pass


mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
  "api_key": mailchimp_api_key,
  "server": mailchimp_server
})

list_id = mailchimp_list_id

member_info = {
    "email_address": "prudence.mcvankab@example.com",
    "status": "subscribed",
    "merge_fields": {
      "FNAME": "Prudence",
      "LNAME": "McVankab"
    }
  }

try:
  response = mailchimp.lists.add_list_member(list_id, member_info)
  print("response: {}".format(response))
except ApiClientError as error:
  print("An exception occurred: {}".format(error.text))