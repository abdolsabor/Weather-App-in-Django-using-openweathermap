from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.

def index(request):

    if request.method == 'POST':
        city = request.POST.get('city')
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + 'api key here').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }


    else:
        city = ''
        data = {}
    #return HttpResponse('<h1> hello </h1>')
    return render(request, 'index.html', {'city':city, 'data':data})

