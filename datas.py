from datetime import datetime

def getForecast(forecastJson):

    five_day_temp_list = [round(item['main']['temp']) for item in forecastJson['list'] 
                        if '12:00:00' in item['dt_txt']]

    five_day_weather_list = [item['weather'][0]['main'] for item in forecastJson['list']
                                if '12:00:00' in item['dt_txt']]

    five_day_dates_list = [datetime.strptime(str(item['dt_txt']).split()[0], '%Y-%m-%d').strftime('%m/%d') for item in forecastJson['list'] 
                        if '12:00:00' in item['dt_txt']]

    five_day_weather_icon = [item['weather'][0]['icon'] for item in forecastJson['list']
                                if '12:00:00' in item['dt_txt']]
    
    return five_day_temp_list, five_day_weather_list, five_day_weather_icon, five_day_dates_list

def getCurrent(jsonData):

    d1 = {}
    d1["city"] = jsonData['name']
    d1['description'] = jsonData['weather'][0]['description']
    d1['datetime'] = datetime.utcfromtimestamp(jsonData['dt']).strftime('%a, %b %d')
    d1["icon"] = jsonData['weather'][0]['icon']
    d1["temp"] = jsonData['main']['temp']
    d1["feel"] = jsonData['main']['feels_like']
    d1["humidity"] = jsonData['main']['humidity']
    d1['wind'] = jsonData['wind']['speed']
    d1["cnt"] = jsonData['sys']['country']

    return d1