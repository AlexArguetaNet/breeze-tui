import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    print(getForecast()["weather"])
    
def getForecast():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=charlotte,us&units=imperial&appid={api_key}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return False

if __name__ == "__main__":
    main() 