from importlib import reload

from client import Chatbot

chatbot = Chatbot()
chatbot.response(":build HoaiAn")

chatbot.response(":reset")
output = chatbot.response("may tuoi")
print(output)

chatbot.response(":reset")
output = chatbot.response("ten gi")
print(output)