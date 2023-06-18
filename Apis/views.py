from django.shortcuts import render,HttpResponse
import requests
import json
# Create your views here.

def get_ip_location(ip):
    api_url='https://ipgeolocation.abstractapi.com/v1/?api_key=65b4761ba7d54305bd31800d90e6fba8&ip_address={}'.format(ip)
    res=requests.get(api_url)
    print(res.status_code)
    print(res.content)
    return res.content

def home(request):
    ip=request.META.get('REMOTE_ADDR')
    print(ip)
    res_json=get_ip_location(ip)
    data=json.loads(res_json)
    return HttpResponse('{}'.format(data))