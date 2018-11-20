from engine.hoaian import HoaiAn


def tests():
    LAUGH = [
        "hihi",
        "hi hi"]
    APOLOGY = ["xin lỗi"]

    ASK_NAME = [
        "bạn tên gì", "bạn tên gì thế",
        "mày tên là gì ?", "tên gì", "tên là gì",
        "Hoài An", "Hoài An à",
        "em tên gì"
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
    ASK_LOCATION = [
        "bạn sống ở đâu",
        "sống ở đâu",
        "ở đâu",
        "cậu quê ở đâu",
        "cậu từ đâu tới",
        "cậu đến từ đâu"
    ]
    ASK_TODAY = [
        "hôm nay cậu vui không",
        "hôm nay thế nào",
        "ngủ ngon không"
    ]
    ASK_KNOWLEDGE = [
        "cậu biết gì",
        "cậu có thể làm gì"
    ]
    AGREEMENT = ["ok"]
    MASTER = ["có biết anh vũ anh không",
              "có biết anh vũ anh không?",
              "vũ anh là ai",
              "tác giả là ai"
              ]
    APPEARANCE = [
        "hoài an xinh không", "cậu xinh ko", "cậu có xinh không"
    ]
    EXCEPTION = [
        ":))", "=)"
    ]
    COLLECTION = [
        LAUGH,
        AGREEMENT, APOLOGY,
        ASK_NAME, ASK_GENDER, ASK_AGE, ASK_LOCATION,
        ASK_TODAY,
        ASK_KNOWLEDGE,
        MASTER,
        APPEARANCE,
        EXCEPTION
    ]
    # COLLECTION = [
    #     ASK_KNOWLEDGE
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
