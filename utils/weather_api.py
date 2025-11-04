import requests, datetime
from modules.forecast import Forecast
from modules.three_day_forecast import Three_Day_Forecast
from utils.env_config import api_key

def get_forecast(location):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location["city"]},{location["country"]}&units=imperial&appid={api_key}")
        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": data["name"],
                "dt": 0,
                "desc": data["weather"][0]["description"],
                "temp": data["main"]["temp"],
                "wind": data["wind"]
            }

            return {"cod": 200, "forecast": Forecast(weather)}
        else:
            return response.json()
        
    except requests.exceptions.ConnectionError as e:
        print(e)
        return e
    

def get_formatted_date(unix_timestamp):
    local_datetime = datetime.datetime.fromtimestamp(unix_timestamp)
    return local_datetime

    
def get_3_day_forecast(location):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={location["city"]},{location["country"]}&appid={api_key}&units=imperial")
        
        if response.status_code == 200:
            
            data = response.json()
            res_days = data["list"]
            city = data["city"]["name"]
            country = data["city"]["country"]
            days = []

            
            for i in range(4):

                dt = get_formatted_date(res_days[i]["dt"])

                weather = {
                    "city": city,
                    "desc": res_days[i]["weather"][0]["description"],
                    "temp": res_days[i]["main"]["temp"],
                    "wind": res_days[i]["wind"],
                    "dt": dt
                }

                days.append(Forecast(weather))

            forecast = Three_Day_Forecast(city, country, days)

            return forecast.__str__()                 

        else:
            return response.json()


    except requests.exceptions.ConnectionError as e:
        print(e)
        return e
    


