from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        req = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4f24bdc7fbebf35d235d3c0987941dc9')
        json_data = json.loads(req)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
