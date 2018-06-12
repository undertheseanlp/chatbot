from engine import bot


def tests():
    print("$ python chatbot_test.py")
    messages = [
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
        "có biết anh vũ anh không",
        "có biết anh vũ anh không?",
        "vũ anh là ai",
        "kém quá",
        "giỏi thật",
    ]
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
