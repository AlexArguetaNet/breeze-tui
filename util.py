import os
from dotenv import load_dotenv
import requests
from modules.forecast import Forecast
from simple_term_menu import TerminalMenu
import sys

load_dotenv()
api_key = os.getenv("API_KEY")

def get_curr_location():
    try:
        with open("curr_location.txt") as file:
            line = file.readline()
            if line:
                city, country = line.split(",")
                city = city.replace(" ", "+")
                return {"city": city, "country": country}
            else:
                return None
    except FileNotFoundError:
        return None
    
def set_curr_location():
    try:
        city = input("Enter your city: ")
        country = input("Enter country code: ")
        if city and country:
            with open("curr_location.txt", "w") as file:
                file.write(f"{city},{country}")
        return {"city": city, "country": country}

    except ValueError:
        return None
    
def get_forecast(location):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location["city"]},{location["country"]}&units=imperial&appid={api_key}")
    if response.status_code == 200:
        data = response.json()

        weather = {
            "city": data["name"],
            "desc": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
            "wind": data["wind"]
        }

        return Forecast(weather)
    else:
        return None
    
def create_menu(options, title):
    menu = TerminalMenu(options, title=title)
    return menu.show()

def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")