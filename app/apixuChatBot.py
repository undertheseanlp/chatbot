import requests
import pprint

KEY = "e312e89387d7487386e163240180804"
URL = "http://api.apixu.com"
pp = pprint.PrettyPrinter(indent=2)

def get_history_weather(args=None):
    url = URL + "/v1/history.json"
    params = {}
    params['key'] = KEY
    params['lang'] = "vi"
    if args != None:
        params.update(args)
    response = requests.get(url,params).json()
    return convert_history(response)


def convert_history(data):
    if "error" in data :
        return convert_error(data)
    else :
        data = data['forecast']['forecastday']
        res = []
        for i in data:
            res.append({
                "thiên văn học": {
                    "mặt trăng mọc": i['astro']['moonrise'],
                    "mặt trăng lặn": i['astro']['moonset'],
                    "mặt trời mọc": i['astro']['sunrise'],
                    "mặt trời lặn": i['astro']['sunset']
                },
                "độ ẩm trung bình": str(i['day']['avghumidity']),
                "nhiệt độ trung bình (độ C)": str(i['day']['avgtemp_c']),
                "tầm nhìn trung bình (km)": str(i['day']['avgvis_km']),
                "điều kiện thời tiết": i['day']['condition']['text'],
                "nhiệt độ tối đa (độ C)": str(i['day']['maxtemp_c']),
                "tốc độ gió tối đa (km/h)": str(i['day']['maxwind_kph']),
                "nhiệt độ thấp nhất (độ C)": str(i['day']['mintemp_c']),
                "tổng lượng mưa (mm)": str(i['day']['totalprecip_mm']),
                "uv": str(i['day']['uv'])
            })
        return res[0]


def get_data_current_weather(args=None):
    url = URL + "/v1/current.json"
    params = {}
    params['key'] = KEY
    params['lang'] = "vi"
    if args != None:
        params.update(args)
    response = requests.get(url, params).json()
    return convert_current(response)


def convert_current(data):
    if 'error' in data :
        return convert_error(data)
    else :
        data = data['current']
        return {
            "mây" : data['cloud'],
            "điều kiện thời tiết" : data['condition']['text'],
            "nhiệt độ cảm nhận (độ C)" : "30",
            "độ ẩm" : "94",
            "ban ngày" : "đúng",
            "lượng mưa (mm)" : str(data['precip_mm']),
            "áp suất khí quyển (millibars)" : str(data['pressure_mb']),
            "nhiệt độ (độ C)" : str(data['temp_c']),
            "tầm nhìn (km)" : str(data['vis_km']),
            "hướng gió (độ góc)" : str(data['wind_degree']),
            "hướng gió (la bàn)" : data['wind_dir'],
            "tốc độ gió (km/h)" : data['wind_kph']
        }


def get_forecast_weather(args=None):
    url = URL + "/v1/forecast.json"
    params = {}
    params['key'] = KEY
    params['lang'] = "vi"
    if args != None:
        params.update(args)
    response = requests.get(url, params).json()
    return convert_forecast(response)


def convert_forecast(data) :
    if 'error' in data:
        return convert_error(data)
    else :
        data = data['forecast']['forecastday']
        res = []
        for i in data :
            res.append({
                "thiên văn học" : {
                    "mặt trăng mọc" : i['astro']['moonrise'],
                    "mặt trăng lặn" : i['astro']['moonset'],
                    "mặt trời mọc" : i['astro']['sunrise'],
                    "mặt trời lặn" : i['astro']['sunset']
                },
                "độ ẩm trung bình" : str(i['day']['avghumidity']),
                "nhiệt độ trung bình (độ C)" : str(i['day']['avgtemp_c']),
                "tầm nhìn trung bình (km)" : str(i['day']['avgvis_km']),
                "điều kiện thời tiết" : i['day']['condition']['text'],
                "nhiệt độ tối đa (độ C)" : str(i['day']['maxtemp_c']),
                "tốc độ gió tối đa (km/h)" : str(i['day']['maxwind_kph']),
                "nhiệt độ thấp nhất (độ C)" : str(i['day']['mintemp_c']),
                "tổng lượng mưa (mm)" : str(i['day']['totalprecip_mm']),
                "uv" : str(i['day']['uv'])
            })
        return res[0]


def convert_error(data) :
    if data['error']['code'] == 1002 :
        return {"error":"api key không tìm thấy"}
    elif data['error']['code'] == 1003 :
        return {"error": "không được cung cấp địa điểm"}
    elif data['error']['code'] == 1005 :
        return {"error": "api không đúng"}
    elif data['error']['code'] == 1006 :
        return {"error": "địa điểm không tìm thấy"}
    elif data['error']['code'] == 1007 :
        return {"error": "thời gian không chính xác"}
    elif data['error']['code'] == 2006 :
        return {"error": "api key không chính xác"}
    elif data['error']['code'] == 2007 :
        return {"error": "api key vượt quá số lần truy cập"}
    elif data['error']['code'] == 2008 :
        return {"error": "api key bị disabled"}
    elif data['error']['code'] == 9999 :
        return {"error": "lỗi ứng dụng nội bộ ???"}


if __name__ == "__main__":
    # params = {}
    # params['q'] = "hanoi"
    # params['key'] = KEY
    # params['dt'] = "2018 - 04 - 09"
    # params['lang'] = "vi"
    # args = {'q':'hanoi','dt':"2018 - 05 - 08",'hour':12}
    # json_data = get_forecast_weather(args)
    # pp.pprint(json_data)

    pp.pprint(get_data_current_weather({'q':'123'}))
    # pp.pprint(get_history_weather({'q':'hanoi','dt':'2018 - 05 - 2'}))

