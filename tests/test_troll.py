from engine.hoaian import HoaiAn


def tests():
    TROLL = ["a", "a", "a", "b", "a", "a", "a", "a", "a", "a", "xin lỗi"]
    COLLECTION = [
        TROLL,
    ]
    # COLLECTION = [
    #     APPEARANCE
    # ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = HoaiAn.reply("localuser", message)
        print("Bot>", reply)


if __name__ == '__main__':
    tests()
