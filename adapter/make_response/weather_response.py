from app import apixuChatBot as api
import datetime

def make_msg(data):
    response = query_api({"loc": data['LOC'], "time": data['TIME'], "weather": data['WEATHER']})
    return response

def query_api(data):
    res = []
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    locs = data['loc']
    times = data['time']
    weather = data['weather']
    for loc in locs :
        for time in times :
            args = {"q":"{},{}".format(loc['lat'],loc['lng']),"dt":"{}-{}-{}".format(time['year'],time['month'],time['day'])}
            if datetime.date(current_year,current_month,current_day) < datetime.date(int(time['year']),int(time['month']),int(time['day'])) :
                res.append(api.get_forecast_weather(args))
            elif datetime.date(current_year,current_month,current_day) == datetime.date(int(time['year']),int(time['month']),int(time['day'])):
                res.append(api.get_data_current_weather(args))
            else :
                res.append(api.get_history_weather(args))
    return filter_msg(res,weather,locs,times)


def filter_msg( data, weather, locs, times):
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
                        print(z)
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