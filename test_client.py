from importlib import reload

from client import Chatbot

chatbot = Chatbot()
chatbot.response(":build HoaiAn")

chatbot.response(":reset")
output = chatbot.response("hi")
print(output)

chatbot.response(":reset")
output = chatbot.response("tên gi")
print(output)