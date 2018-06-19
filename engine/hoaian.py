from os.path import dirname, join
from rivescript import RiveScript
from core import post_process
from core.world import FACTS

hoaian_bot = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "hoaian")
hoaian_bot.load_directory(engine_folder)
hoaian_bot.sort_replies()

class HoaiAn:
    @staticmethod
    def reply(uid, text):
        if hoaian_bot.get_uservar(uid, "facts") is None:
            print("set fact hoai an the hell")
            hoaian_bot.set_uservars(uid, {"facts": FACTS})
        text = post_process(text)
        response = hoaian_bot.reply(uid, text)
        return response
