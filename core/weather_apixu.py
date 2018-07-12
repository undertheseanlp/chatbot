from core import apixuChatBot as api
from core import location_detection
from core import date_detection
from core import time_detection
import datetime


def weather_api(time, loc, weather):
    locationDetect = location_detection.LocationDetector()
    time_convert = convert_time([time])
    loc_lat_long = locationDetect.detect_location(loc)

    response_api = query_api({"loc": [loc_lat_long], "time": time_convert, "weather": ["thời tiết"]})
    filter_response = filter_msg(response_api, ["thời tiết"], [loc_lat_long], time_convert)
    response = response_msg(filter_response, weather, time)
    return response


def convert_time(data):
    timeDetector = time_detection.TimeDetector()
    dateDetector = date_detection.DateDetector()
    data_time = []
    for time in data:
        sub_time = timeDetector.detect_time(time)
        sub_date = dateDetector.detect_date(time)
        for i in sub_time:
            for j in sub_date:
                sub_data = {}
                sub_data.update(i)
                sub_data.update(j)
                data_time.append(sub_data)
    return fill_time(data_time)


def fill_time(data):
    months = []
    years = []
    data_time = []
    current_time = datetime.datetime.now()
    for date in data:
        if date['month'] != None:
            months.append(date['month'])
        if date['year'] != None:
            years.append(date['year'])
    for date in data:
        if date['day'] == None and date['month'] == None and date['year'] == None:
            if len(data) > 1:
                continue
            else:
                data_time.append({
                    "day": current_time.day,
                    "month": current_time.month,
                    "year": current_time.year,
                    "hour": date['hour'],
                    "minute": date['minute']
                })
        elif date['day'] == None and date['month'] != None and date['year'] == None:
            if len(years) > 0:
                data_time.append({
                    "day": "1",
                    "month": date['month'],
                    "year": years[0],
                    "hour": date['hour'],
                    "minute": date['minute']
                })
            else:
                data_time.append({
                    "day": "1",
                    "month": date['month'],
                    "year": current_time.year,
                    "hour": date['hour'],
                    "minute": date['minute']
                })
        elif date['day'] == None and date['month'] != None and date['year'] != None:
            data_time.append({
                "day": "1",
                "month": date['month'],
                "year": date['year'],
                "hour": date['hour'],
                "minute": date['minute']
            })
        elif date['day'] != None and date['month'] == None and date['year'] == None:
            if len(months) > 0:
                if len(years) > 0:
                    data_time.append({
                        "day": date['day'],
                        "month": months[0],
                        "year": years[0],
                        "hour": date['hour'],
                        "minute": date['minute']
                    })
                else:
                    data_time.append({
                        "day": date['day'],
                        "month": months[0],
                        "year": current_time.year,
                        "hour": date['hour'],
                        "minute": date['minute']
                    })
            else:
                data_time.append({
                    "day": date['day'],
                    "month": current_time.month,
                    "year": current_time.year,
                    "hour": date['hour'],
                    "minute": date['minute']
                })
        elif date['day'] != None and date['month'] != None and date['year'] == None:
            if len(years) > 0:
                data_time.append({
                    "day": date['day'],
                    "month": date['month'],
                    "year": years[0],
                    "hour": date['hour'],
                    "minute": date['minute']
                })
            else:
                data_time.append({
                    "day": date['day'],
                    "month": date['month'],
                    "year": current_time.year,
                    "hour": date['hour'],
                    "minute": date['minute']
                })
        elif date['day'] == None and date['month'] == None and date['year'] != None:
            data_time.append({
                "day": "1",
                "month": "1",
                "year": date['year'],
                "hour": date['hour'],
                "minute": date['minute']
            })
        elif date['day'] != None and date['month'] != None and date['year'] != None:
            data_time.append(date)
    return data_time


def query_api(data):
    res = []
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    locs = data['loc']
    times = data['time']
    weather = data['weather']
    for loc in locs:
        for time in times:
            args = {"q": "{},{}".format(loc['lat'], loc['lng']),
                    "dt": "{}-{}-{}".format(time['year'], time['month'], time['day'])}
            if datetime.date(current_year, current_month, current_day) < datetime.date(int(time['year']),
                                                                                       int(time['month']),
                                                                                       int(time['day'])):
                res.append(api.get_forecast_weather(args))
            elif datetime.date(current_year, current_month, current_day) == datetime.date(int(time['year']),
                                                                                          int(time['month']),
                                                                                          int(time['day'])):
                res.append(api.get_data_current_weather(args))
            else:
                res.append(api.get_history_weather(args))
    return res


def filter_msg(data, weather, locs, times):
    w = ['nắng', 'mưa', 'nhiệt độ', 'mây', 'độ ẩm', 'gió', 'tầm nhìn', 'áp suất khí quyển', 'uv', 'lượng mưa',
         'hướng gió', 'nóng', 'lạnh', 'rét', 'thời tiết']
    er = []
    enable_data = []
    res = {}
    for i in weather:
        if i not in w:
            er.append("không có dữ liệu về {} :(".format(i))
        else:
            enable_data.append(i)
    res['error'] = er
    filter_data = []
    sat = []
    for loc in locs:
        for time in times:
            sat.append((time, loc))
    # for tup in sat:
    for id, i in enumerate(data):
        d = {}
        d["thời tiết"] = {}
        for k in enable_data:
            if k in ["thời tiết"]:
                d["thời tiết"] = i
                break
            elif k in ["nắng"]:
                for z in i:
                    if "nhiệt độ" in z or "mây" in z or "lượng mưa" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["nhiệt độ", "nóng", "lạnh", "rét"]:
                for z in i:
                    if "nhiệt độ" in z or "mây" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["mưa", "lượng mưa"]:
                for z in i:
                    if "lượng mưa" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["mây"]:
                for z in i:
                    if "mây" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["tầm nhìn"]:
                for z in i:
                    if "tầm nhìn" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["uv"]:
                for z in i:
                    if "uv" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["hướng gió", "gió"]:
                for z in i:
                    if "gió" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["áp suất khí quyển"]:
                for z in i:
                    if "áp suất" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["độ ẩm"]:
                for z in i:
                    if "độ ẩm" in z or "lượng mưa" in z:
                        d["thời tiết"][z] = i[z]
        time = sat[id][0]
        loc = sat[id][1]
        d['thời gian'] = "{}/{}/{}".format(time['day'], time['month'], time['year'])
        d['địa điểm'] = loc['name']
        filter_data.append(d)
    res['data'] = filter_data
    return res


def return_msg(filter_msg):
    msg = ''
    for i in range(len(filter_msg['data'])):
        msg += " Tại " + str(filter_msg['data'][i]['địa điểm']).title() + " " + str(
            filter_msg['data'][i]['thời gian']) + ': '
        for k, v in filter_msg['data'][i]['thời tiết'].items():
            if isinstance(v, dict):
                msg += str(k) + ":  "
                for i, j in v.items():
                    msg += ", "
            else:
                msg += str(k) + " : " + str(v)
            msg += ", "
    return msg


def response_msg(filter_msg, weather, time):
    dict_temperature = ['nhiệt độ', 'nóng', 'lạnh', 'rét', 'nắng']
    dict_rain = ['mưa', 'bão']

    loc = str(filter_msg['data'][0]['địa điểm']).title()
    weather_data = filter_msg['data'][0]['thời tiết']
    weather_response = ""
    rain_response = ""
    temperature_response = ""
    temperature = float(filter_msg['data'][0]['thời tiết']['nhiệt độ trung bình (độ C)'])
    if temperature > 34:
        temperature_response = "rất nóng"
    elif temperature > 28:
        temperature_response = "nóng"
    elif temperature > 20:
        temperature_response = "mát mẻ"
    elif temperature > 14:
        temperature_response = "lạnh"
    temperature_response += " nhiệt độ khoảng " + str(temperature) + " độ C"
    rain = float(filter_msg['data'][0]['thời tiết']['tổng lượng mưa (mm)'])
    if rain == 0.0:
        rain_response += "không mưa"
    else:
        rain_response += "có mưa"

    if weather in dict_rain:
        weather_response += rain_response
    elif weather in dict_temperature:
        weather_response += temperature_response
    else:
        weather_response += temperature_response + ", " + rain_response
    msg = loc + " " + time + " " + weather_response

    return msg
