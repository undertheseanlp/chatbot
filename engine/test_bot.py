from engine import bot


def tests():
    print("$ python chatbot_test.py")
    SIMPLE = [
        "bạn tên gì",
        "mày tên là gì ?",
        "bạn bao nhiêu tuổi",
        "bạn sống ở đâu",
        "bạn tên gì",  # reask
        "bạn tên gì",  # reask
        "cậu bao nhiêu tuổi?",
        "cậu bao nhiêu tuổi",
        "bạn mấy tuổi",
        "cậu bao nhiêu tuổi rồi ?",
        "cậu là ai",
        "kém quá",
        "giỏi thật",
        "Hoài An",
        "Hoài An à",
        "đồ ngu",
        "mẹ mày",
        "như cứt"
    ]
    APOLOGY = ["xin lỗi"]
    GREETING = ["tạm biệt"]
    HACK = ["a", "a", "a", "b", "a", "a", "a", "a", "a", "a", "xin lỗi", "a", "a"]
    MASTER = ["có biết anh vũ anh không",
              "có biết anh vũ anh không?",
              "vũ anh là ai"]
    COLLECTION = [
        SIMPLE, GREETING, MASTER, APOLOGY, HACK
    ]
    # COLLECTION = [
    #     HACK
    # ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = bot.reply("localuser", message)
        print("Bot>", reply)


def start_bot():
    while True:
        msg = input('You> ')
        if msg == '/quit':
            quit()

        reply = bot.reply("localuser", msg)
        print('Bot>', reply)


if __name__ == '__main__':
    # start_bot()
    tests()
