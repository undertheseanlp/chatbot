from engine.hoaian import HoaiAn


def tests():
    TROLL = [
        ("u1", ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]),
        ("u2", ["a", "b", "c", "a"])
    ]

    for talk in TROLL:
        user, messages = talk
        for message in messages:
            print("{} >".format(user), message)
            reply = HoaiAn.reply(user, message)
            print("Bot>", reply)


if __name__ == '__main__':
    tests()
