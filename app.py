from flask import Flask, request, render_template
import requests
from datetime import datetime
from datas import getCurrent, getForecast

app = Flask(__name__)


@app.route('/')
def showApp():
    return render_template('index.html')

@app.route('/weather', methods=['POST' , "GET"])
def weatherUpdate():
    url = "https://api.openweathermap.org/data/2.5/weather"
    urlForecast = "http://api.openweathermap.org/data/2.5/forecast"

    param = {
        'q': request.form.get('location'),
        'appid': request.form.get('apikey'),
        'units':'metric'
    }
    
    response = requests.get(url, params=param)
    currenData = getCurrent(response.json())

    responseForecast = requests.get(urlForecast, params=param)
    five_day_temp_list, five_day_weather_list, five_day_weather_icon, five_day_dates_list = getForecast(responseForecast.json())

    
    return render_template('weather.html', data=currenData, five_day_temp_list=five_day_temp_list, 
                           five_day_weather_list=five_day_weather_list, five_day_weather_icon=five_day_weather_icon, 
                           five_day_dates_list=five_day_dates_list)

if __name__ == '__main__':
    app.run(debug=True)
