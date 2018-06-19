from engine.hoaian import HoaiAn

Bot = HoaiAn


def tests():
    ANGRY = [
        "mẹ",
        "im đi"
    ]
    VULGARITY = [
        "mẹ mày",
        "như cứt",
        "dm"
    ]
    CURSE = [
        "đồ ngu",
        "kém quá",
        "bot ngu",
        "con bot ngu này",
        "ngu thật",
        "ngu vậy",
        "cái đồ đần này",
        "cái loz"
    ]
    COMPLIMENT = [
        "giỏi thật",
    ]
    BOREDOM = [
        "chán vãi"
    ]
    COLLECTION = [
        ANGRY,
        VULGARITY,
        CURSE, BOREDOM,
        COMPLIMENT
    ]

    # COLLECTION = [
    #     BOREDOM
    # ]

    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = Bot.reply("localuser", message)
        print("Bot>", reply)


if __name__ == '__main__':
    tests()
