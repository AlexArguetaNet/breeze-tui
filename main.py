from utils.location_storage import get_curr_location, set_curr_location
from utils.weather_api import get_forecast, get_3_hourly_forecast
from utils.cli_helpers import create_menu, clear_terminal
from utils.weather_api import get_units, set_units
import sys

def main():
    
    while True:
        # Try to get the current forecast data
        clear_terminal()
        
        units = get_units()
        if not units:
            set_units()

        forecast_res = get_forecast(get_curr_location(), units)

        if forecast_res["cod"] == "404":
            # Case that curr_location.txt doesn't exist 
            # or curr_location.txt is empty
            print("Enter a valid location")
            set_curr_location()
            continue
        else:
            # Case that current location is valid
            curr_forecast = forecast_res["forecast"] # Get forecast object
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
    match option:
        case 0:
            get_curr_location()
            set_curr_location()
        case 1:
            #TODO: Implement function to change units
            units_option = create_menu(["Imperial", "Metric"], "Units")
            match units_option:
                case 0:
                    set_units()
                case 1:
                    set_units("metric")
        case _:
            pass
        


    
if __name__ == "__main__":
    main() 