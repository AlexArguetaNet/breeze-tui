import os
from dotenv import load_dotenv
import requests
from util import get_curr_location, set_curr_location

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    curr_location = get_curr_location()
    if not curr_location:
        curr_location = set_curr_location()
        print("Location set!")

    print(curr_location)
    
def get_forecast(location):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location["city"]},us&units=imperial&appid={api_key}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    

if __name__ == "__main__":
    main() 