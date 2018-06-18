from engine.hoaian import HoaiAn


def tests():
    print("$ python chatbot_test.py")

    SAY_NAME = [
        "mình tên là cường",
        "tớ tên là nhật tinh anh",
    ]

    COLLECTION = [
        SAY_NAME
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
