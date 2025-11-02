from modules.forecast import Forecast

class Three_Day_Forecast:
    def __init__(self, city, country, days):
        self.city = city
        self.country = country
        self.days = days

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        self._country = country

    @property
    def days(self):
        return self._days
    @days.setter
    def days(self, days):
        self._days = days

    def __str__(self):
        forecast_str = f"{self.city}\n"
        days_str = ""

        for day in self.days:
            days_str = days_str + f"{day.get_ascii()}\n{day.temp}\n{day.desc}    "

        return forecast_str + days_str

            

