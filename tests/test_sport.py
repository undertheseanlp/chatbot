from engine.hoaian import HoaiAn


def tests():

    SIMPLE = [
        "abcdef"
    ]

    COLLECTION = [
        SIMPLE
    ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = HoaiAn.reply("localuser", message)
        print("Bot>", reply)


if __name__ == '__main__':
    tests()
