from importlib import reload

from client import Chatbot

chatbot = Chatbot()

chatbot.response(":reset")
output = chatbot.response("may tuoi")
print(output)

chatbot.response(":reset")
output = chatbot.response("cậu bao nhiêu tuổi")
print(output)