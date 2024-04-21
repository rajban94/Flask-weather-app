from datetime import datetime

def getForecast(forecastJson):

    fivedaymax = {}
    for item in forecastJson['list']:
        if item['dt_txt'].split(" ")[0] != str(datetime.now()).split(" ")[0]:
            fivedaymax.setdefault(item['dt_txt'].split(" ")[0],[]).append(round(item['main']['temp_max']))
    
    fivedaymin = {}
    for item in forecastJson['list']:
        if item['dt_txt'].split(" ")[0] != str(datetime.now()).split(" ")[0]:
            fivedaymin.setdefault(item['dt_txt'].split(" ")[0],[]).append(round(item['main']['temp_min']))
    
    five_day_temp_list = []

    for date in fivedaymax:
        max_temp = max(fivedaymax[date])
        min_temp = min(fivedaymin[date])
        temp = str(min_temp)+"/"+str(max_temp)
        five_day_temp_list.append(temp)

    five_day_weather_list = [item['weather'][0]['main'] for item in forecastJson['list']
                                if '00:00:00' in item['dt_txt'] and item['dt_txt'].split(" ")[0] != str(datetime.now()).split(" ")[0]]

    five_day_dates_list = [datetime.strptime(str(item['dt_txt']).split()[0], '%Y-%m-%d').strftime('%m/%d') for item in forecastJson['list'] 
                        if '00:00:00' in item['dt_txt']and item['dt_txt'].split(" ")[0] != str(datetime.now()).split(" ")[0]]

    five_day_weather_icon = [item['weather'][0]['icon'] for item in forecastJson['list']
                                if '00:00:00' in item['dt_txt'] and item['dt_txt'].split(" ")[0] != str(datetime.now()).split(" ")[0]]
    
    return five_day_temp_list, five_day_weather_list, five_day_weather_icon, five_day_dates_list

def getCurrent(jsonData):

    d1 = {}
    d1["city"] = jsonData['name']
    d1['description'] = jsonData['weather'][0]['description']
    d1['datetime'] = datetime.utcfromtimestamp(jsonData['dt']).strftime('%a, %b %d')
    d1["icon"] = jsonData['weather'][0]['icon']
    d1["temp"] = round(jsonData['main']['temp'])
    d1["feel"] = round(jsonData['main']['feels_like'])
    d1["humidity"] = jsonData['main']['humidity']
    d1['wind'] = jsonData['wind']['speed']
    d1["cnt"] = jsonData['sys']['country']
    d1['sunrise'] = datetime.utcfromtimestamp(jsonData['sys']['sunrise'] + jsonData['timezone']).strftime('%I:%M %p')
    d1['sunset'] = datetime.utcfromtimestamp(jsonData['sys']['sunset']  + jsonData['timezone']).strftime('%I:%M %p')

    return d1