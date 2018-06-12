import requests


api_key = "4c265ca828093a8f1934bb65efb1090c"
location = "Ha Noi"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric&mode=json".format(
    location, api_key)
url = "http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}&units=metric&mode=json".format(
    location, api_key)
r = requests.get(url)
print(0)
