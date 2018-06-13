from engine.hoaian import HoaiAn

Bot = HoaiAn

def tests():
    WEATHER = [
        "thời tiết hôm nay",
        "thời tiết hôm nay thế nào",
        "thời tiết hôm nay như thế nào",
        "thời tiết hôm nay thế nào?",
        "thời tiết hôm nay như thế nào?",
        "hôm nay thời tiết thế nào",
        "hôm nay thời tiết thế nào?"
    ]
    COLLECTION = [
        WEATHER
    ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = Bot.reply(message)
        print("Bot>", reply)


if __name__ == '__main__':
    tests()
