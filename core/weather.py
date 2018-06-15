from core.location import Location
from core.timeutil import TimeUtil
from core.weather_darksky import WeatherRepository


def analyze(weather_data, duration):
    """ analyze weather data
    Parameters
    ----------
    duration : blank, đêm, sáng, trưa, chiều, tối

    Returns
    -------
    rain_summary and temperature_summary in duration
    """
    data = weather_data["hourly"]["data"]
    statuses = [item["icon"] for item in data]
    temperatures = [item["temperature"] for item in data]
    if "rain" in statuses:
        rain_summary = "CÓ_MƯA"
    else:
        rain_summary = "KHÔNG_MƯA"
    temperature_avg = sum(temperatures) / len(temperatures)
    if temperature_avg > 34:
        temperature_summary = "RẤT_NÓNG"
    elif temperature_avg > 28:
        temperature_summary = "NÓNG"
    elif temperature_avg > 20:
        temperature_summary = "MÁT_MẺ"
    elif temperature_avg > 14:
        temperature_summary = "LẠNH"
    else:
        temperature_summary = "RẤT_LẠNH"
    output = {
        "rain_summary": rain_summary,
        "temperature_summary": temperature_summary
    }
    return output


def summary(location_name="Ha Noi", time_string="HÔM_NAY", duration=""):
    location = Location.search(location_name)
    timestamp = TimeUtil.start_of_day(time_string)
    weather_data = WeatherRepository.get_weather(location_id=location["id"], timestamp=timestamp)
    weather = analyze(weather_data, duration)
    output = ""

    if time_string == "HÔM_NAY":
        output += "hôm nay trời "
    elif time_string == "NGÀY_MAI":
        output += "ngày mai trời "
    elif time_string == "HÔM_QUA":
        output += "hôm qua trời "
    output += weather["temperature_summary"].replace("_", " ").lower()
    output += ", "
    output += weather["rain_summary"].replace("_", " ").lower()
    return output


if __name__ == '__main__':
    times = ["HÔM_KIA", "HÔM_QUA", "HÔM_NAY", "NGÀY_MAI", "NGÀY_KIA"]
    for time_string in times:
        weather_summary = summary(time_string=time_string)
        print("{}: {}".format(time_string, weather_summary))