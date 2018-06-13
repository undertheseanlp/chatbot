from core.location import LOCATIONS
from core.timeutil import TimeUtil
from core.weather_darksky import WeatherRepository

for location in LOCATIONS:
    location_id, name, lat, long = location
    print(name)
    for date in range(12, 16):
        print("{}/06/2018".format(date))
        timestamp = TimeUtil.timestamp(2018, 6, date)
        data = WeatherRepository.get_weather(location_id, timestamp)
        status = " ".join([item["icon"] for item in data["hourly"]["data"]])
        temperature = " ".join([str(item["temperature"]) for item in data["hourly"]["data"]])
        print(status)
        print(temperature)
