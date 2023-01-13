from django.shortcuts import HttpResponse
from datetime import datetime
# Create your views here.

def hello(requests):
    if requests.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date(requests):
    current_date = datetime.now()
    if requests.method == 'GET':
        return HttpResponse(current_date)


def goodbye(requests):
    if requests.method == 'GET':
        return HttpResponse("Goodbye user!")