from flask import Flask
from dotenv import load_dotenv
import os
import requests
app = Flask(__name__)

# Load API key from .env
load_dotenv()
API_KEY = os.getenv('API_KEY')
URL = f"https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    if not API_KEY:
        return{
            "message":"Api key is not set in the environment"
        }, 500
    context={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(URL,params=context)
        if response.status_code == 200:
            data=response.json()
            return {
            "status":"success",
            "city":city,
            "temperature":data["main"]["temp"],
            "weather":data["weather"][0]["description"]
            },200
          #  Return actual weather data as JSON
        else:
          return {"status":False,
                  "message": "Failed to fetch weather data"
                  }, response.status_code
      
    except Exception as e:
        return {
            "message":"Failed to Fetch weather data",
            "details":str(e)
        }, 500

if __name__ == '__main__':
    app.run(debug=True)
   