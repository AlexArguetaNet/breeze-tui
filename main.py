from utils.location_storage import get_curr_location, set_curr_location, get_recent_locations, add_recent_location
from utils.weather_api import get_forecast, get_3_hourly_forecast
from utils.cli_helpers import create_menu, clear_terminal
from utils.weather_api import get_units, set_units
import sys

location_changed = False
is_recent_location = True

def main():

    global location_changed
    global is_recent_location
    
    while True:
        # Try to get the current forecast data
        clear_terminal()
        
        units = get_units()
        if not units:
            set_units()

        forecast_res = get_forecast(get_curr_location(), units)
        clear_terminal() # Clear loading prompt

        if forecast_res["cod"] == "404":
            # Case that curr_location.txt doesn't exist 
            # or curr_location.txt is empty
            print("Enter a valid location")
            set_curr_location()
            continue
        else:

            if location_changed and not is_recent_location:
                add_recent_location(get_curr_location())
                location_changed = False

            # Case that current location is valid
            curr_forecast = forecast_res["forecast"] # Get forecast object
            menu_option = create_menu(["Forecast for the next few hours", "Settings", "Exit"], f"\n{curr_forecast.__str__()}\n")
            if menu_option == 0:
                # TODO: Implement 3 day forecast option
                clear_terminal()
                three_hourly_forecast = get_3_hourly_forecast(get_curr_location(), units)
                option = create_menu(["Back"], three_hourly_forecast)
                if option:
                    continue

            elif menu_option == 1:
                handle_settings()
            else:
                sys.exit()

def handle_settings():
    option = settings_menu = create_menu(["Location", "Units", "Back"], "Settings")
    match option:
        case 0:
            change_location()
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
        
def change_location():
    global location_changed
    global is_recent_location

    menu_options = ["Enter new", "Choose from list"]
    recent_locations = get_recent_locations()
    if recent_locations != None:
        menu_options.append("Recent")


    option = create_menu(menu_options, "Location")

    match (option):
        case 0:
            # Set a new location
            set_curr_location()
            is_recent_location = False
        case 1:
            # TODO: Implement list of default locations
            ...
        case 2:
            new_location_index = create_menu(recent_locations, "Choose")

            # Run this code if an option was selected
            if new_location_index:
                city, country = recent_locations[new_location_index].split(",")
                set_curr_location({"city": city, "country": country})
                is_recent_location = True
    
    location_changed = True
    
        

    

    
if __name__ == "__main__":
    main() 