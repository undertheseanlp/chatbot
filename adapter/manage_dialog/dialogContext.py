from adapter.intend import adapterIntend
from adapter.greeting import adapterGreeting
from adapter.ner_crf import adapterNer
import json
from adapter.manage_dialog import manageDialog as manager
from adapter.make_response import weather_response as res
adapterIntend = adapterIntend.AdapterIntend()
adapterNer = adapterNer.AdapterNer()
adapterGreeting = adapterGreeting.AdapterGreeting()

def response(request):
    data = data = json.loads(request.body.decode("utf-8"))
    user_msg = data["text"]
    intend = adapterIntend.get_intend(user_msg)
    print(intend)
    # return intend
    if  manager.getState(request)== 1:
        if intend == 1:
            data = adapterGreeting.make_response(user_msg)
        elif intend == 2:
            data = adapterNer.detect_entity(user_msg)
        elif intend == 3:
            data = adapterNer.detect_entity(user_msg)
        else:
            data = None
        return make_msg(request,data, intend)
    elif manager.getState(request) == 2:
        if intend == 1:
            data = adapterGreeting.make_response(user_msg)
        elif intend == 2:
            data = adapterNer.detect_entity(user_msg)
        elif intend == 3:
            data = adapterNer.detect_entity(user_msg)
        else:
            data = adapterNer.detect_entity(user_msg)
        return make_msg(request,data, intend)
    elif manager.getState(request) == 3:
        data = adapterNer.detect_entity(user_msg)
        if adapterNer.detect_question_again(user_msg):
            data = adapterNer.detect_entity(user_msg)
            print("Hihhi", data)
            return make_msg(request,data, intend)
        else:
            manager.updateState(request,1)
            manager.updateTime(request,None)
            manager.updateLoc(request,None)
            if intend == 1:
                data = adapterGreeting.make_response(user_msg)
            elif intend == 2:
                data = adapterNer.detect_entity(user_msg)
            elif intend == 3:
                data = adapterNer.detect_entity(user_msg)
            else:
                data = None
            return make_msg(request,data, intend)


def make_msg(request,data=None, intend=4):
    data_msg = {}
    if manager.getState(request) == 3:
        if data['LOC'] == [] and data['TIME'] == [] and data['WEATHER'] == []:
            manager.updateLoc(request,[])
            manager.updateTime(request,[])
            manager.updateWeather(request,["thời tiết"])
            manager.updateMsg(request,"mình không hiểu ý bạn :(")
            manager.updateState(request,1)
        else:
            if data['LOC'] != []:
                manager.updateLoc(request,data['LOC'])
            if data['TIME'] != []:
                manager.updateTime(request,data['TIME'])

            if len(data["WEATHER"]) != 0:
                manager.updateWeather(request, data["WEATHER"])
                manager.updateState(request,3)
            res_msg= res.query_api(
            {"loc": manager.getLoc(request), "time": manager.getTime(request),"weather": manager.getWeather(request)})
            manager.updateMsg(request,res_msg)

    else:
        if intend == 1:
            manager.updateLoc(request,[])
            manager.updateTime(request,[])
            manager.updateWeather(request,["thời tiết"])
            manager.updateMsg(request,data)
            manager.updateState(request,1)
        elif intend == 2:
            if data['LOC'] != []:
                manager.updateLoc(request,data['LOC'])
            if data['TIME'] != []:
                manager.updateTime(request,data['TIME'])
            if len(data["WEATHER"]) == 0 and manager.getWeather(request)== []:
                manager.updateWeather(request,["thời tiết"])
            elif len(data['WEATHER']) == 0:
                manager.updateWeather(request,manager.getWeather(request))
            else:
                manager.updateWeather(request,data["WEATHER"])

            if manager.getLoc(request) == None or manager.getLoc(request) == []:
                manager.updateMsg(request, "bạn cho xin địa điểm :D")
                manager.updateState(request,2)
            elif manager.getTime(request) == None or manager.getTime(request) == []:
                manager.updateMsg(request, "bạn cho xin thời gian :D")
                manager.updateState(request,2)
            else:
                res_msg = res.query_api(
                    {"loc": manager.getLoc(request), "time": manager.getTime(request), "weather": manager.getWeather(request)})
                manager.updateMsg(request,res_msg)
                manager.updateState(request,3)

        elif intend == 3:
            if data['LOC'] != []:
                manager.updateLoc(request,data['LOC'])
            if data['TIME'] != []:
                manager.updateTime(request,data['TIME'])
            if len(data["WEATHER"]) == 0 and manager.getWeather(request) == []:
                manager.updateWeather(request, ["thời tiết"])
            elif len(data['WEATHER']) == 0:
                manager.updateWeather(request,manager.getWeather(request))
            else:
                manager.updateWeather(request,data["WEATHER"])

            if manager.getLoc(request) == None or manager.getLoc(request) == []:
                manager.updateMsg(request, "bạn cho xin địa điểm :D")
                manager.updateState(request,2)
            elif manager.getTime(request) == None or manager.getTime(request) == []:
                manager.updateMsg(request, "bạn cho xin thời gian :D")
                manager.updateState(request,2)
            else:
                res_msg = res.query_api(
                    {"loc": manager.getLoc(request), "time": manager.getTime(request), "weather": manager.getWeather(request)})
                manager.updateMsg(request,res_msg)
                manager.updateState(request,3)

        elif intend == 4 and manager.getState(request) == 1:
            manager.updateLoc(request,None)
            manager.updateTime(request,None)
            manager.updateWeather(request,["thời tiết"])
            manager.updateMsg(request,"mình không hiểu ý bạn :(")
            manager.updateState(request,1)

        elif intend == 4 and manager.getState(request) == 2:
            if data["LOC"] != []:
                manager.updateLoc(request,data['LOC'])
            if data["TIME"] != []:
                manager.updateTime(request,data['TIME'])
            if len(data["WEATHER"]) == 0:
                manager.updateWeather(request,manager.getWeather(request))
            else:
                manager.updateWeather(request,data["WEATHER"])

            if manager.getLoc(request) == None or manager.getLoc(request) == []:
                manager.updateMsg(request, "bạn cho xin địa điểm :D")
                manager.updateState(request,2)
            elif manager.getTime(request) == None or manager.getTime(request) == []:
                manager.updateMsg(request, "bạn cho xin thời gian :D")
                manager.updateState(request,2)
            else:
                res_msg = res.query_api(
                    {"loc": manager.getLoc(request), "time": manager.getTime(request), "weather": manager.getWeather(request)})
                manager.updateMsg(request,res_msg)
                manager.updateState(request,3)

    data_msg["intend"] = intend
    data_msg["loc"] = manager.getLoc(request)
    data_msg["time"] = manager.getTime(request)
    data_msg["weather"] = manager.getWeather(request)
    data_msg["msg"] = manager.getMsg(request)
    data_msg["state"] = manager.getState(request)
    return data_msg

