from engine.hoaian import HoaiAn


def tests():
    print("$ python chatbot_test.py")
    GREETING_HELLO = ["hi"]
    GREETING_BYE = ["tạm biệt", "bye an"]
    GREETING_HRU = ["khoe khong", "Bạn có khỏe không", "khỏe không?", "Khoẻ không"]
    COLLECTION = [
        GREETING_HELLO, GREETING_BYE, GREETING_HRU
    ]
    # COLLECTION = [
    #     ASK_AGE
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
