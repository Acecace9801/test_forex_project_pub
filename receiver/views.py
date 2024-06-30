from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import *


def send_message(message):
    token = "7408547471:AAG3uEjVnwwrRHzw7VsjLFEJ-16HeB2QdAY"
    chat_id = "1008005908"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()


# Create your views here.
def index(request):
    response_data = {
        'status': '200',
        'message': 'x',
    }
    return JsonResponse(response_data)


@csrf_exempt
def api_scanner_update_id(request, name):
    request.session['init'] = True
    data = json.loads(request.body)
    accountNumber = data.get('accountNumber')
    scanner, _ = Scanner.objects.get_or_create(
        accountNumber=accountNumber if accountNumber else 0
    )
    scanner.brokerName = data.get('brokerName')
    scanner.currentEquity = data.get('currentEquity')
    scanner.totalSwap = data.get('totalSwap')
    scanner.longSwap = data.get('longSwap')
    scanner.shortSwap = data.get('shortSwap')
    scanner.message = "api_scanner_update_id"
    scanner.save()
    response_data = {
        'status': '200',
        'message': "Success",
    }
    return JsonResponse(response_data)


@csrf_exempt
def api_scanner(request):
    data = json.loads(request.body)
    accountNumber = data.get('accountNumber')
    scanner, _ = Scanner.objects.get_or_create(
        accountNumber=accountNumber if accountNumber else 0
    )
    scanner.brokerName = data.get('brokerName')
    scanner.currentEquity = data.get('currentEquity')
    scanner.totalSwap = data.get('totalSwap')
    scanner.longSwap = data.get('longSwap')
    scanner.shortSwap = data.get('shortSwap')
    scanner.message = "api_scanner_update_id"
    scanner.save()
    return JsonResponse({'status': '200', 'message': 'Success'})


@csrf_exempt
def api_scanner_update(request):
    return JsonResponse({'status': '200', 'message': 'Hello', 'id': 'x'})


def test(request):
    scanner = Scanner.objects.all().order_by('-updated_at').values()[:10]
    context = {
        'scanner': scanner,
    }
    return render(request, 'receiver/test.html', context)
