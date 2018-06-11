from os.path import dirname, join
from rivescript import RiveScript

bot = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "simple")
bot.load_directory(engine_folder)
bot.sort_replies()