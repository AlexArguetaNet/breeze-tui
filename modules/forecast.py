import utils.art as art
import math

class Forecast:
    def __init__(self, weather):
        self._city = weather["city"]
        self._desc = weather["desc"]
        self._temp = str(weather["temp"]).split(".")[0]
        self._wind = weather["wind"]
        self._dt = weather["dt"]
        self._units = weather["units"] 

    @property
    def city(self):
        return self._city

    @property
    def desc(self):
        return self._desc

    @property
    def temp(self):
        return self._temp
    
    @property
    def wind(self):
        return self._wind

    @property
    def dt(self):
        return self._dt
    
    @property
    def units(self):
        return self._units
    
    def get_unit_symbol(self):
        if self.units == "imperial":
            return "F"
        else:
            return "C"

    @property
    def get_ascii(self):
        return self._ascii

    def get_ascii(self):
        match self.desc:
            case "clear sky":
                return art.sun
            case "few clouds":
                return art.sun_and_cloud
            case "scattered clouds":
                return art.sun_and_cloud
            case "broken clouds":
                return art.sun_and_cloud
            case "shower rain":
                return art.rain
            case "rain":
                return art.rain
            case "thunderstorm":
                return art.thunder_storm
            case "snow":
                return art.snow
            case "light snow":
                return art.snow
            case "mist":
                return art.mist
            case "drizzle":
                return art.rain
            case "heavy intensity rain":
                return art.rain
            case "moderate rain":
                return art.rain
            case "overcast clouds":
                return art.clouds
            case "light rain":
                return art.rain
            case "light intensity drizzle":
                return art.rain
            case _:
                return "image"
            
    def __str__(self):
        return f"{self.city}\n{self.get_ascii()}\n{self.temp} {self.get_unit_symbol()}°\n{self.desc}"

