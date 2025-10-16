
def get_curr_location():
    try:
        with open("curr_location.txt") as file:
            line = file.readline()
            if line:
                location = line.split(",")
                return {"city": location[0], "country": location[1]}
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