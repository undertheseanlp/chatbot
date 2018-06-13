# Darksky
import json
from os import listdir, mkdir
from os.path import dirname, join

import requests

from core.location import LOCATIONS
from core.timeutil import TimeUtil

token = "358f3308204f06c44d3ea28ed7e14cfe"


class WeatherAPI:
    @staticmethod
    def get_weather(location_id, timestamp):
        global token
        item = [location for location in LOCATIONS if location[0] == location_id][0]
        location_id, name, lat, long = item
        # example https://api.darksky.net/forecast/358f3308204f06c44d3ea28ed7e14cfe/21.0278,105.8342,1528822800?units=si
        url_format = "https://api.darksky.net/forecast/{}/{},{},{}?units=si"
        url = url_format.format(token, lat, long, timestamp)
        r = requests.get(url)
        data = r.json()
        return data


class WeatherRepository:
    REPO_PATH = join(dirname(dirname(__file__)), "data", "weather")

    @staticmethod
    def get_weather(location_id, timestamp):
        if WeatherRepository.exist(location_id, timestamp):
            return WeatherRepository.load(location_id, timestamp)
        else:
            data = WeatherAPI.get_weather(location_id, timestamp)
            WeatherRepository.save(location_id, timestamp, data)
            return data

    @staticmethod
    def exist(location_id, timestamp):
        REPO_PATH = WeatherRepository.REPO_PATH
        if location_id not in listdir(REPO_PATH):
            mkdir(join(REPO_PATH, location_id))
            return False
        path = join(REPO_PATH, location_id)
        filename = "{}.txt".format(timestamp)
        if filename not in listdir(path):
            return False
        return True

    @staticmethod
    def save(location_id, timestamp, data):
        path = join(WeatherRepository.REPO_PATH, location_id, "{}.txt".format(timestamp))
        with open(path, "w") as f:
            f.write(json.dumps(data))

    @staticmethod
    def load(location_id, timestamp):
        path = join(WeatherRepository.REPO_PATH, location_id, "{}.txt".format(timestamp))
        with open(path) as f:
            content = f.read()
            data = json.loads(content)
            return data
        return None


if __name__ == '__main__':
    for location in LOCATIONS:
        location_id, name, lat, long = location
        for date in range(10, 14):
            timestamp = TimeUtil.timestamp(2018, 6, date)
            WeatherRepository.get_weather(location_id, timestamp)
    print("Done")
