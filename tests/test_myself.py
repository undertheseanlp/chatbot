from engine.hoaian import HoaiAn


def tests():
    print("$ python chatbot_test.py")
    GREETING_HELLO = ["hi"]
    GREETING_BYE = ["tạm biệt"]
    GREETING_HRU = ["khoe khong", "Bạn có khỏe không", "khỏe không?", "Khoẻ không"]
    LAUGH = ["hihi", "hi hi"]
    APOLOGY = ["xin lỗi"]

    ASK_NAME = [
        "bạn tên gì", "bạn tên gì thế",
        "mày tên là gì ?", "tên gì", "tên là gì",
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
              "vũ anh là ai",
              "tác giả là ai"
              ]
    APPEARANCE = ["hoài an xinh không", "cậu xinh ko"]
    EXCEPTION = [
        ":))", "=)", "b"
    ]
    COLLECTION = [
        GREETING_HELLO, GREETING_BYE, GREETING_HRU,
        LAUGH,
        AGREEMENT, APOLOGY,
        SIMPLE,
        ASK_NAME, ASK_GENDER, ASK_AGE, ASK_LOCATION, MASTER,
        APPEARANCE,
        HACK,
        CURSE,
        EXCEPTION
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
