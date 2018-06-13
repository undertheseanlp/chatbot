from core.location import LOCATIONS, Location
from core.timeutil import TimeUtil
from core.weather_darksky import WeatherRepository

def analyze_weather_by_locations():
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

if __name__ == '__main__':
    # analyze_weather_by_locations()
    timestamp = TimeUtil.timestamp(2018, 6, 15)
    # timestamp = 1528768800
    location_name = "Ha Noi"
    location = Location.search(location_name)
    data = WeatherRepository.get_weather(location["id"], timestamp)
    print("DONE")