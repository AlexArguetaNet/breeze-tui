from utils.location_storage import get_curr_location, set_curr_location
from utils.weather_api import get_forecast
from utils.cli_helpers import create_menu, clear_terminal
import sys

def main():
    curr_location = get_curr_location()
    if not curr_location:
        curr_location = set_curr_location()
        print("Location set!")

    curr_forecast = get_forecast(curr_location)
    if not curr_forecast:
        print("An error occured. Please check your internet connection.")
        sys.exit()
    
    while True:
        clear_terminal()
        menu_option = create_menu(["3 Day Forecast", "Set Location", "Exit"], curr_forecast.__str__())
        if menu_option == 0:
            # TODO: Implement 3 day forecast option
            ...
        elif menu_option == 1:
            # Set new location
            new_location = set_curr_location()
            curr_forecast = get_forecast(new_location)
        else:
            sys.exit()
    
if __name__ == "__main__":
    main() 