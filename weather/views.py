import requests
from django.shortcuts import render

def index(request):
    appid='7bb22b66e96d4bfba289943498c913e8'
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city='London'
    res=requests.get(url.format(city)).json()
    city_info={
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context={'info': city_info}
    return render(request, 'weather/index.html', context)