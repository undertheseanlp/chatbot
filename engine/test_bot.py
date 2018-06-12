from core import post_process
from engine import bot


def tests():
    print("$ python chatbot_test.py")
    SIMPLE = [
        "bạn tên gì",
        "mày tên là gì ?",
        "bạn bao nhiêu tuổi",
        "bạn sống ở đâu",
        "bạn là ai",
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
        "mẹ mày",
        "như cứt"
    ]
    CURSE = [
        "đồ ngu",
        "bot ngu"
    ]
    INFORMATION = [
        "cậu là nam hay nữ vậy",
        "cậu là nam hay nữ thế",
        "cậu là nam hay nữ"
    ]
    APOLOGY = ["xin lỗi"]
    GREETING = ["tạm biệt"]
    AGREEMENT = ["ok"]
    HACK = ["a", "a", "a", "b", "a", "a", "a", "a", "a", "a", "xin lỗi"]
    MASTER = ["có biết anh vũ anh không",
              "có biết anh vũ anh không?",
              "vũ anh là ai"]
    SPECIAL_CHARACTERS = [
        ":))", "=)", "b"
    ]
    COLLECTION = [
        SIMPLE, INFORMATION,
        GREETING, MASTER, HACK,
        CURSE, APOLOGY, AGREEMENT,
        SPECIAL_CHARACTERS
    ]
    # COLLECTION = [
    #     INFORMATION
    # ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        message = post_process(message)
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
