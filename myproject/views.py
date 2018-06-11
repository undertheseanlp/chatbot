from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from engine import bot


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def chatbot(request):
    result = {}
    try:
        text = json.loads(request.body.decode("utf-8"))["text"]
        response_message = bot.reply("localuser", text)
        result["output"] = response_message
    except:
        result = {"error": "Bad request!"}
    return JsonResponse(result)
