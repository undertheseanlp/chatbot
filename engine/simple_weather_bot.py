from os.path import dirname, join
from rivescript import RiveScript
from core import post_process
from core.weather import summary

bot = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "simple")
bot.load_directory(engine_folder)
bot.sort_replies()


class SimpleWeatherBot:
    @staticmethod
    def is_match_weather(text):
        patterns = [
            "thời tiết hôm nay",
            "thời tiết hôm nay thế nào",
            "thời tiết hôm nay như thế nào",
            "thời tiết hôm nay thế nào?",
            "thời tiết hôm nay như thế nào?",
            "hôm nay thời tiết thế nào",
            "hôm nay thời tiết thế nào?"
        ]
        if text in patterns:
            return True
        return False

    @staticmethod
    def weather_reply(text):
        return summary()

    @staticmethod
    def reply(text):
        if SimpleWeatherBot.is_match_weather(text):
            return SimpleWeatherBot.weather_reply(text)
        text = post_process(text)
        response = bot.reply("localuser", text)
        return response
