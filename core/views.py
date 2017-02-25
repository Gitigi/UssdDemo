from django.shortcuts import render
from ussd.core import UssdView, UssdRequest
from django.conf import settings
from django.http import HttpResponse
import os,json
from core.models import Customer
path = os.path.join(settings.BASE_DIR, "core")

def get_balance(request):
    phoneNumber = request.GET.get('phoneNumber','+25345435445')
    customer,exitst = Customer.objects.get_or_create(phoneNumber=phoneNumber)
    response = {'balance':customer.balance}
    return HttpResponse(json.dumps(response),content_type='application/json')

def top_up(request):
    phoneNumber = request.GET.get('phoneNumber', '+25345435445')
    customer, exitst = Customer.objects.get_or_create(phoneNumber=phoneNumber)
    customer.balance += int(request.GET['domination'])
    customer.save()
    response = {'status':'OK','balance':customer.balance}
    return HttpResponse(json.dumps(response),content_type='application/json')

class Sample(UssdView):
    customer_journey_namespace = "DemoUssdGateway"
    customer_journey_conf = path + "/journey.yml"

    def post(self, req):
        data = req.data
        return UssdRequest(
            phone_number=data['phoneNumber'].strip('+'),
            session_id=data['sessionId'],
            ussd_input=data['text'],
            language=data.get('language', 'en')
        )

    def get(self, req):
        data = req.GET
        return UssdRequest(
            phone_number=data['phoneNumber'].strip('+'),
            session_id=data['sessionId'],
            ussd_input=data['text'],
            language=data.get('language', 'en')
        )
