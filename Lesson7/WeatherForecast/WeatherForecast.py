import requests
import json
from datetime import datetime, timedelta

from urllib3.util import url


class WeatherForecast:
    def __init__(self, filepath="weather_record.json", latitude=18.02945850, longitude=48.315658):
        self.filepath = filepath
        self.latitude = latitude
        self.longitude = longitude

        #loading cache
        try:
            with open(self.filepath, "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}


    #-------INTERFACES-------
    def __getitem__(self, date):
        if date in self.data:
            return self.data[date]["Rain"]

        #When not cached, go to API
        rain = self._fetch_from_api(date)
        self.data[date] = {"Rain": rain}
        self._save()
        return rain

    def __setitem__(self, date, value): #to assign stuff
        self.data[date] = {"Rain": value}
        self._save()

    def __iter__(self):
        #for date in weather_forecast...
        return iter(self.data.keys())

    def items(self):
        #weather_forecast.items()
        for date, info in self.data.items():
            yield date, info["Rain"]

    #-------INTERNAL METHODS-------

    def _fetch_from_api(self, date):
        # original API link
        # https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={self.latitude}&longitude={self.longitude}"
            f"&daily=precipitation_sum"
            f"&timezone=Europe%2FLondon"
            f"&start_date={date}&end_date={date}"
        )

        try:
            response = requests.get(url)
            result = response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        if response.status_code != 200:
            raise ValueError(f"HTTP Error: {response.status_code}")

        if "error" in result:
            raise ValueError(result.get("reason", "Unknown API error"))

        rain_list = result["daily"]["precipitation_sum"]
        return float(rain_list[0])

    def _save(self):
        with open(self.filepath, "w") as file:
            json.dump(self.data, file, indent=4)