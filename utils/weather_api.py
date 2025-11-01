import requests
from modules.forecast import Forecast
from utils.env_config import api_key

def get_forecast(location):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location["city"]},{location["country"]}&units=imperial&appid={api_key}")
        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": data["name"],
                "desc": data["weather"][0]["description"],
                "temp": data["main"]["temp"],
                "wind": data["wind"]
            }

            return {"cod": 200, "forecast": Forecast(weather)}
        else:
            return response.json()
        
    except requests.exceptions.ConnectionError as e:
        return e
    
    

# def get_forecast(location):
#     response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location["city"]},{location["country"]}&units=imperial&appid={api_key}")
#     if response.status_code == 200:
#         data = response.json()

#         weather = {
#             "city": data["name"],
#             "desc": data["weather"][0]["description"],
#             "temp": data["main"]["temp"],
#             "wind": data["wind"]
#         }

#         return Forecast(weather)
#     else:
#         return None