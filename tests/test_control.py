from engine.hoaian import HoaiAn

HoaiAn.reply(":build HoaiAn", "local")
HoaiAn.reply(":reset", "local")

def talk(input_text):
    print("user:", input_text)
    reply = HoaiAn.reply(input_text, user="local")
    print("bot:", reply)

talk("Chào cậu")
for i in range(10):
    talk("???")

