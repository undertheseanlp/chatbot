import requests
import pprint

KEY = "ae545a312764e6b225534a5d7f7b2a27"

# API_ADDRESS = "http://api.openweathermap.org/data/2.5/weather?units=metric&appid=ae545a312764e6b225534a5d7f7b2a27&q="
# CITY = input('City Name :')
# URL = API_ADDRESS + CITY

URL2 = "http://history.openweathermap.org/data/2.5/history/city?id=2885679&type=hour&appid=ae545a312764e6b225534a5d7f7b2a27"

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    json_data = requests.get(URL2).json()
    # format_add = json_data['base']
    pp.pprint(json_data)