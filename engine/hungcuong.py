from os.path import dirname, join
from rivescript import RiveScript
from core import post_process
from core.world import FACTS

hungcuong_bot = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "hungcuong")
hungcuong_bot.load_directory(engine_folder)
hungcuong_bot.sort_replies()


class HungCuong:
    @staticmethod
    def reply(uid, text):
        if hungcuong_bot.get_uservar(uid, "facts") is None:
            hungcuong_bot.set_uservars(uid, {"facts": FACTS.copy()})
        text = post_process(text)
        response = hungcuong_bot.reply(uid, text)
        return response
