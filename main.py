from utils.location_storage import get_curr_location, set_curr_location
from utils.weather_api import get_forecast, get_3_hourly_forecast
from utils.cli_helpers import create_menu, clear_terminal
import sys

def main():
    
    while True:
        # Try to get the current forecast data
        clear_terminal()
        forecast_res = get_forecast(get_curr_location())

        if forecast_res == None:
            # Case that curr_location.txt doesn't exist 
            # or curr_location.txt is empty
            set_curr_location()
            continue
        else:
            # Case that current location is valid
            curr_forecast = forecast_res["forecast"]
            menu_option = create_menu(["Forecast for the next few hours", "Settings", "Exit"], f"\n{curr_forecast.__str__()}\n")
            if menu_option == 0:
                # TODO: Implement 3 day forecast option
                clear_terminal()
                three_hourly_forecast = get_3_hourly_forecast(get_curr_location())
                option = create_menu(["Back"], three_hourly_forecast)
                if option:
                    continue

            elif menu_option == 1:
                handle_settings()
            else:
                sys.exit()

def handle_settings():
    option = settings_menu = create_menu(["Set new location", "Change units", "Back"], "Settings")


def change_location():
    og_location = get_curr_location()
    new_location = set_curr_location()
    forecast_res = get_forecast(new_location)

    if forecast_res["cod"] == "404" and forecast_res["message"] == "city not found":
        print("Invalid location")
        set_curr_location(og_location)
        return None
    else:
        return get_curr_location, forecast_res["forecast"]
        


    
if __name__ == "__main__":
    main() 