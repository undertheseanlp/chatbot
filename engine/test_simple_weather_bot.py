from core import post_process
from engine.simple_weather_bot import SimpleWeatherBot


def tests():
    print("$ python chatbot_test.py")
    BASIC = [
        "bạn tên gì",
        "mày tên là gì ?",

    ]
    WEATHER = [
        "thời tiết hôm nay thế nào"
    ]
    COLLECTION = [
        BASIC, WEATHER
    ]
    # COLLECTION = [
    #     INFORMATION
    # ]
    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = SimpleWeatherBot.reply(message)
        print("Bot>", reply)


def start_bot():
    while True:
        msg = input('You> ')
        if msg == '/quit':
            quit()
        reply = SimpleWeatherBot.reply("localuser", msg)
        print('Bot>', reply)


if __name__ == '__main__':
    # start_bot()
    tests()
