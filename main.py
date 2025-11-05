from utils.location_storage import get_curr_location, set_curr_location
from utils.weather_api import get_forecast, get_3_day_forecast
from utils.cli_helpers import create_menu, clear_terminal
import sys

def main():

    # Try to get the current location
    curr_location = get_curr_location()
    if not curr_location: # If curr_location.txt doesn't exist
        curr_location = set_curr_location()

    while True:
        
        forecast_res = get_forecast(curr_location)

        if forecast_res["cod"] == 200:
            break
        elif forecast_res["cod"] == "404" and forecast_res["message"] == "city not found":
            print("Invalid location")
            curr_location = set_curr_location()
            pass
        else:
            print(forecast_res["message"])
            sys.exit()

    # Getting Forecast object from successful response
    curr_forecast = forecast_res["forecast"]
    
    while True:
        clear_terminal()
        menu_option = create_menu(["Fore for the next few hours", "Set Location", "Exit"], f"\n{curr_forecast.__str__()}\n")
        if menu_option == 0:
            # TODO: Implement 3 day forecast option
            clear_terminal()
            three_day_forecast = get_3_day_forecast(curr_location)
            option = create_menu(["Back"], three_day_forecast)
            if option:
                continue

        elif menu_option == 1:

            # Set new location
            og_location = get_curr_location()
            new_location = set_curr_location()
            forecast_res = get_forecast(new_location)

            if forecast_res["cod"] == "404" and forecast_res["message"] == "city not found":
                print("Invalid location")
                set_curr_location(og_location)
                pass
            else:
                curr_location = new_location
                curr_forecast = forecast_res["forecast"]


        else:
            sys.exit()
    
if __name__ == "__main__":
    main() 