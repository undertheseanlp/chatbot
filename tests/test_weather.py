from engine.hoaian import HoaiAn

Bot = HoaiAn


def tests():
    WEATHER = [
        # "thời tiết hôm qua thế nào",
        # "thời tiết hôm nay",
        # "thời tiết hôm nay thế nào",
        # "thời tiết hôm nay như thế nào",
        "hôm nay thời tiết thế nào",
        "thời tiết ngày mai thế nào",
        "ngày mai thời tiết thế nào",
        "hôm nay mưa hay nắng",
        "hôm nay trời đẹp thế",
        "hôm nay trời có mưa không",
        "dự đoán hôm nay thời tiết",
        "dự đoán thời tiết hôm nay",
        "dự báo thời tiết hôm nay thế nào?",
        "mai Hà Nội có mưa không thế?"
    ]
    COMPARE = [
        "hôm nay nắng hơn hôm qua không?",

    ]
    COLLECTION = [
        WEATHER,
        COMPARE
    ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = Bot.reply("localuser", message)
        print("Bot>", reply)


if __name__ == '__main__':
    HoaiAn.init()
    tests()
