from engine.hoaian import HoaiAn

Bot = HoaiAn

def tests():
    MATH = [
        "1 + 1",
        "5 + 7",
        "41 - 6",
    ]
    SHORT_CHARACTER = [
        "b"
    ]
    COLLECTION = [
        MATH,
        SHORT_CHARACTER
    ]
    COLLECTION = [
        SHORT_CHARACTER
    ]

    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = Bot.reply("localuser", message)
        print("Bot>", reply)


if __name__ == '__main__':
    tests()
