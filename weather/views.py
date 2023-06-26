import requests
from django.shortcuts import render
from .models import City

def index(request):
    appid='7bb22b66e96d4bfba289943498c913e8'
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities=City.objects.all()
    all_cities=[]
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info={
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context={'all_info': all_cities}
    return render(request, 'weather/index.html', context)

def info(request):
    context={}
    return render(request, 'weather/info.html', context)

def documents(request):
    context={}
    return render(request, 'weather/documents.html', context)