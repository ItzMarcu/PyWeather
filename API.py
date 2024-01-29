import requests
import eel

eel.init('static-web')

@eel.expose
def getWeather(city):
    apiKey = "4997e4f5d81fb6c42b907e6b1670f696"
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': apiKey
    }

    try: 
        response = requests.get(baseUrl, params=params)
        data = response.json()
        weatherDescription = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"{weatherDescription}, Temperatura: {temperature}"
    except Exception as e: 
        return f"Error: {e}"

eel.start('static-web/index.html', size = (400, 600))