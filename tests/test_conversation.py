from engine.hoaian import HoaiAn


def tests():
    print("$ python chatbot_test.py")
    GREETING_HELLO = ["hi"]
    GREETING_BYE = ["tạm biệt"]
    GREETING_HRU = ["khoe khong", "Bạn có khỏe không", "khỏe không?", "Khoẻ không"]
    UNKNOWN_ANSWER = [
        "Roger là ai"
    ]
    CONFUSE = [
        "?"
    ]
    TOPIC_FINDING = [
        "command topic finding"
    ]
    COLLECTION = [
        GREETING_HELLO, GREETING_BYE, GREETING_HRU,
        UNKNOWN_ANSWER,
        CONFUSE
    ]
    COLLECTION = [
        TOPIC_FINDING
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
