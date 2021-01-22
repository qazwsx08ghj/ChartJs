from django.shortcuts import render
from chart.models import datas

import requests
import random


def chart_view(request):

    if len(datas.objects.all()) is not 0:
        pass
    else:
        create_data()

    r = requests.get('http://127.0.0.1:8000/api/datas/?format=json')
    num = [number['number'] for number in r.json()]
    v = [value['value'] for value in r.json()]

    return render(request, 'chart.html', {'number': num, 'value': v})


def create_data():
    for index in range(10):
        r = requests.post('http://127.0.0.1:8000/api/datas/create', data={'value': random.randint(1, 100)})
    return r.status_code
