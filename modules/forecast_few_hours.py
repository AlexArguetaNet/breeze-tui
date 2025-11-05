from modules.forecast import Forecast

class Forecast_Few_Hours:
    def __init__(self, city, country, days):
        self._city = city
        self._country = country
        self._days = days

    @property
    def city(self):
        return self._city

    @property
    def country(self):
        return self._country

    @property
    def days(self):
        return self._days

    def __str__(self):
        forecast_str = f"{self.city}\n"
        days_str = "-----------------------"

        for day in self.days:
            days_str = days_str + f"\n{day.dt}{day.get_ascii()}\n{day.temp}\n{day.desc}\n-----------------------"

        return forecast_str + days_str

            

