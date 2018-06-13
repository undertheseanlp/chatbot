from engine.simple_bot import SimpleBot


def tests():
    print("$ python chatbot_test.py")
    SIMPLE = [

        "kém quá",
        "giỏi thật",
        "mẹ mày",
        "như cứt"
    ]
    GREETING_HELLO = ["hi"]
    GREETING_BYE = ["tạm biệt"]
    GREETING_HRU = ["Bạn có khỏe không", "khỏe không?"]
    LAUGH = ["hihi", "hi hi"]
    APOLOGY = ["xin lỗi"]
    CURSE = [
        "đồ ngu",
        "bot ngu"
    ]
    ASK_NAME = [
        "bạn là ai", "cậu là ai",
        "bạn tên gì",  "bạn tên gì",  # reask
        "mày tên là gì ?",
        "Hoài An", "Hoài An à",
    ]
    ASK_GENDER = [
        "cậu là nam hay nữ vậy",
        "cậu là nam hay nữ thế",
        "cậu là nam hay nữ", "nam hay nữ"
    ]
    ASK_AGE = [
        "bạn bao nhiêu tuổi",
        "cậu bao nhiêu tuổi?",
        "bạn mấy tuổi",
        "cậu bao nhiêu tuổi rồi ?",
    ]
    ASK_LOCATION = ["bạn sống ở đâu"]
    AGREEMENT = ["ok"]
    HACK = ["a", "a", "a", "b", "a", "a", "a", "a", "a", "a", "xin lỗi"]
    MASTER = ["có biết anh vũ anh không",
              "có biết anh vũ anh không?",
              "vũ anh là ai"]
    EXCEPTION = [
        ":))", "=)", "b"
    ]
    COLLECTION = [
        GREETING_HELLO, GREETING_BYE, GREETING_HRU,
        LAUGH,
        AGREEMENT, APOLOGY,
        SIMPLE,
        ASK_NAME, ASK_GENDER, ASK_AGE, ASK_LOCATION, MASTER ,
        HACK,
        CURSE,
        EXCEPTION
    ]
    # COLLECTION = [
    #     INFORMATION
    # ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = SimpleBot.reply(message)
        print("Bot>", reply)


def start_bot():
    while True:
        msg = input('You> ')
        if msg == '/quit':
            quit()

        reply = SimpleBot.reply("localuser", msg)
        print('Bot>', reply)


if __name__ == '__main__':
    # start_bot()
    tests()
