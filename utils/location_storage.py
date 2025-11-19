from utils.cli_helpers import create_menu

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
    
def set_curr_location(location=""):
    try:
        if location == "":
            city = input("Enter your city: ")
            country = input("Enter country code: ")
            if city and country:
                with open("curr_location.txt", "w") as file:
                    file.write(f"{city},{country}")
            return {"city": city, "country": country}
        else:
            with open("curr_location.txt", "w") as file:
                    file.write(f"{location["city"]},{location["country"]}")         
    except ValueError:
        return None
    
def add_recent_location(location):
    try:
        with open("recent_locations.txt", "a") as file:
            file.write(f"{location["city"]},{location["country"]}" + "\n")
            return location
    except ValueError:
        print("No location given")

def get_recent_locations():
    recent_locations = []
    try:

        with open("recent_locations.txt", "r") as file:
            for line in file:
                line = line.strip()
                city, country = line.split(",")
                city = city.replace("+", " ")
                recent_locations.append(f"{city},{country}")

        recent_locations.reverse()
        return recent_locations
    except FileNotFoundError:
        return None
    
def update_recent_locations(location):
    try:
        
        with open("recent_locations.txt", 'r') as file_in:
            lines = file_in.readlines() # Read all recent locations
            if not lines:
                return False
            
            lines.append(f"{location["city"]},{location["country"]}\n") # Add new location to file
            
        # Write updated file list without first location
        with open("recent_locations.txt", 'w') as file_out:
            file_out.writelines(lines[1:])

    except FileNotFoundError:
        return False
    except ValueError:
        return False
