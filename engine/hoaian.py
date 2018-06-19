from os.path import dirname, join
from rivescript import RiveScript
from core import post_process
from core.world import FACTS

bot = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "hoaian")
bot.load_directory(engine_folder)
bot.sort_replies()
print(0)

class HoaiAn:
    @staticmethod
    def reply(uid, text):
        if not bot.get_uservar(uid, "facts"):
            bot.set_uservars(uid, {"facts": FACTS})
        text = post_process(text)
        response = bot.reply(uid, text)
        return response
