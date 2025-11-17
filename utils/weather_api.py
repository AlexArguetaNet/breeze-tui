import requests, datetime
from modules.forecast import Forecast
from modules.three_hourly_forecast import Three_Hourly_Forecast
from utils.env_config import api_key

def get_units():
    try:
        with open("units.txt", "r") as file:
            line = file.readline().rstrip()
            if line:
                return line
            else:
                return None
    except FileNotFoundError:
        return None
    
def set_units(units="imperial"):
    try:
        with open("units.txt", "w") as file:
            file.write(units)
        return units.rstrip()
    except ValueError:
        return None

def get_forecast(location, units="imperial"):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location["city"]},{location["country"]}&units={units}&appid={api_key}")
        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": data["name"],
                "dt": 0,
                "desc": data["weather"][0]["description"],
                "temp": data["main"]["temp"],
                "wind": data["wind"],
                "units": units
            }

            return {"cod": 200, "forecast": Forecast(weather)}
        else:
            return response.json()
        
    except requests.exceptions.ConnectionError as e:
        print(e)
        return e
    except TypeError:
        return {"cod": "404", "message": "Location file was empty"}
    

def get_formatted_date(unix_timestamp):
    local_datetime = datetime.datetime.fromtimestamp(unix_timestamp)
    formatted_time = local_datetime.strftime("%I:%M %p")
    return formatted_time

    
def get_3_hourly_forecast(location, units="imperial"):
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
                    "dt": dt,
                    "units": units
                }

                days.append(Forecast(weather))

            forecast = Three_Hourly_Forecast(city, country, days)

            return forecast.__str__()                 

        else:
            return response.json()


    except requests.exceptions.ConnectionError as e:
        print(e)
        return e
    

