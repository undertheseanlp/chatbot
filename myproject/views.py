from os.path import dirname, join
from os import listdir, mkdir
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from adapter.intend import adapterIntend
from adapter.greeting import adapterGreeting
from adapter.ner_crf import adapterNer
from adapter.make_response import weather_response
from adapter.manage_dialog import manageDialog
from adapter.manage_dialog import dialogContext
from engine.hoaian import HoaiAn

adapIntend = adapterIntend.AdapterIntend()
adapGreeting = adapterGreeting.AdapterGreeting()
adapNer = adapterNer.AdapterNer()

def index(request):
    manageDialog.initDialog(request)
    return render(request, 'index.html')


def log(text):
    today = datetime.now().strftime('%Y%m%d')
    LOG_FOLDER = join(dirname(dirname(__file__)), "logs")
    log_file = join(LOG_FOLDER, "{}.txt".format(today))
    with open(log_file, "a") as f:
        f.write(text + "\n")


@csrf_exempt
def chatbot(request):
    result = {}
    dialog = dialogContext.response(request)
    print("session")
    print(request.session["loc"])
    print(request.session["time"])
    print(request.session["weather"])
    print(request.session["bot_msg"])
    print("end")
    try:
        data = json.loads(request.body.decode("utf-8"))
        text = data["text"]
        uid = data["uid"]
        ip = request.META["REMOTE_ADDR"]
        time = datetime.now().strftime('%Y%m%d %H:%M:%S')
        log_text = "{} {} {} {}".format(ip, time, "USER:", text)
        log(log_text)
        # response_message = HoaiAn.reply("uid", text)

        intend = adapIntend.get_intend(text)
        if isinstance(dialog['msg'], str):
            response_message = dialog['msg']
        else:
            response_message = weather_response.return_msg(dialog['msg'])
            print(dialog['msg']['data'])

        # if intend is greeting and other
        # if intend == 1 or intend == 4:
        #     response_message = HoaiAn.reply("uid", text)
        #     # response_message = adapGreeting.make_response(text)
        #
        # # if intend is weather question
        # else:
        #
        #     # detect entity from user message
        #     ner_response = adapNer.detect_entity(text)
        #
        #     # return message response to user
        #     results = weather_response.make_msg(ner_response)
        #     response_message = weather_response.return_msg(results)

        log_text = "{} {} {} {}".format(ip, time, "BOT:", response_message)
        log(log_text)

        result["output"] = response_message
    except Exception as e:
        print(e)
        result = {"error": "Bad request!"}
    return JsonResponse(result)


if __name__ == '__main__':
    log("hihi")
