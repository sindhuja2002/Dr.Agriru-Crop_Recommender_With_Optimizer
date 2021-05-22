import requests, json

def weather(city):
 
        api_key = "11c7b470c61ca14dd4028c93ee72f45a"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = city

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        if x['cod'] != "404":

            y = x['main']
            current_temperature = y['temp'] - 273.15
            current_humidity = y['humidity']
            return ( current_temperature, current_humidity)

        else:
            return(25.78 ,50)
    