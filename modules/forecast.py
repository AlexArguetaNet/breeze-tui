import utils.art as art
import math

class Forecast:
    def __init__(self, weather):
        self.city = weather["city"]
        self.desc = weather["desc"]
        self.temp = weather["temp"]
        self.wind = weather["wind"]
        self.ascii = self.set_ascii()

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def desc(self):
        return self._desc
    @desc.setter
    def desc(self, desc):
        self._desc = desc

    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, temp):
        temp = f"{str(temp).split(".")[0]} °"
        self._temp = temp
    
    @property
    def wind(self):
        return self._wind
    @wind.setter
    def wind(self, wind):
        self._wind = wind

    def set_ascii(self):
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
            case _:
                return "image"
            
    def __str__(self):
        return f"\n{self.city}\n{self.ascii}\n{self.temp}\n{self.desc}\n"

