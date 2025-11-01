
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