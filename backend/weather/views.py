import requests
from django.http import JsonResponse
from django.views import View

class WeatherView(View):
    def get(self, request, city):
        api_key = 'your_api_key'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        return JsonResponse(response.json())