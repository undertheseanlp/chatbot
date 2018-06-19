from engine.hoaian import HoaiAn

Bot = HoaiAn


def tests():
    print(Bot.reply("u1", "tớ tên là Cường"))
    print(Bot.reply("u1", "chào"))
    print(Bot.reply("u2", "tớ tên là Long"))
    print(Bot.reply("u2", "chào"))
    print(Bot.reply("u1", "hi"))


if __name__ == '__main__':
    tests()