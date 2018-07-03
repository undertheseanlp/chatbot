from core import weather_apixu as weather
from core import location_detection
from core import date_detection
from core import time_detection

def test_weather_api():
    print(weather.weather_api("mai", "hà nội", "mưa"))

def test_convert_time():
    print(weather.convert_time("mai"))

def test_query_api():
    time_convert = [{'day': '4', 'hour': None, 'year': '2018', 'month': '7', 'minute': None}]
    loc_lat_long = {'lng': 105.8341598, 'lat': 21.0277644, 'name': ' hà nội'}
    print(weather.query_api({"loc": [loc_lat_long], "time": time_convert, "weather": ["thời tiết"]}))

def test_filter_msg():
    time = "mai"
    loc = "hà nội"
    weat = "mưa"
    locationDetect = location_detection.LocationDetector()
    time_convert = weather.convert_time([time])
    loc_lat_long = locationDetect.detect_location(loc)
    # result : time_convert = [{'day': '4', 'hour': None, 'year': '2018', 'month': '7', 'minute': None}]
    # result : loc_lat_long = {'lng': 105.8341598, 'lat': 21.0277644, 'name': ' hà nội'}
    data = weather.query_api({"loc": [loc_lat_long], "time": time_convert, "weather": ["thời tiết"]})
    print(weather.filter_msg(data, [weat], [loc_lat_long], time_convert))

def test_response_msg():
    time = "mai"
    loc = "hà nội"
    weat = "mưa"
    locationDetect = location_detection.LocationDetector()
    time_convert = weather.convert_time([time])
    loc_lat_long = locationDetect.detect_location(loc)
    # result : time_convert = [{'day': '4', 'hour': None, 'year': '2018', 'month': '7', 'minute': None}]
    # result : loc_lat_long = {'lng': 105.8341598, 'lat': 21.0277644, 'name': ' hà nội'}
    data = weather.query_api({"loc": [loc_lat_long], "time": time_convert, "weather": ["thời tiết"]})
    filter_msg = weather.filter_msg(data, ["thời tiết"], [loc_lat_long], time_convert)
    print(weather.response_msg(filter_msg, weat, time))

test_weather_api()

