from django.shortcuts import render
from django.http import HttpResponse
import juspayp3
from random import randint
import requests

juspayp3.api_key = 'D304CC61928C4E67A6519D2CD4639D51'
juspayp3.environment = 'sandbox'

def payment(request):
	random_order_id = randint(100000,200000)
	new_order = juspayp3.Orders.create(
		order_id=random_order_id,
		amount=100.00,
		customer_id='guest_user_101',
		customer_email='customer@gmail.com',
		customer_phone='9988665522',
		return_url='http://127.0.0.1:8910/response'
		)
	param_dict = vars(new_order)
	param_dict['links'] = vars(new_order.payment_links)

	return render(request, 'payment.html', param_dict)

def response(request):
	resp_dict = dict()

	resp_dict['order_id'] = request.GET.get('order_id')
	resp_dict['status'] = request.GET.get('status')
	resp_dict['signature'] = request.GET.get('signature')
	resp_dict['signature_algorithm'] = request.GET.get('signature_algorithm')

	return render(request, 'response.html', resp_dict)
