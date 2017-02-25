from django.shortcuts import render
from ussd.core import UssdView, UssdRequest
from django.conf import settings
from django.http import HttpResponse
import os,json

path = os.path.join(settings.BASE_DIR, "core")

def get_balance(request):
    balance = 45
    print('get balance called')
    response = {'balance':balance}
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
