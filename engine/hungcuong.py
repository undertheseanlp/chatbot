from os.path import dirname, join
from rivescript import RiveScript
from core import post_process

bot = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "hungcuong")
bot.load_directory(engine_folder)
bot.sort_replies()


class HungCuong:
    @staticmethod
    def reply(uid, text):
        text = post_process(text)
        response = bot.reply(uid, text)
        return response
