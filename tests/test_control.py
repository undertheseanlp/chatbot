from engine.hoaian import HoaiAn

HoaiAn.reply("local", ":build HoaiAn")
HoaiAn.reply("local", ":reset")
reply = HoaiAn.reply("loopback", user="anhv")
print(reply)