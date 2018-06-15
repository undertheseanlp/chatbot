from engine.hoaian import HoaiAn

Bot = HoaiAn

def tests():
    print(Bot.reply("u1", "a"))
    print(Bot.reply("u2", "a"))
    print(Bot.reply("u2", "a"))
    print(Bot.reply("u3", "a"))


if __name__ == '__main__':
    tests()
