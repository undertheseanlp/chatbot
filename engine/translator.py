from os.path import dirname, join
from rivescript import RiveScript
from core import post_process

engine = RiveScript(utf8=True)
engine_folder = join(dirname(__file__), "eg", "translator")
engine.load_directory(engine_folder)
engine.sort_replies()


class Translator:
    @staticmethod
    def run(text):
        text = post_process(text)
        response = engine.reply("localuser", text)
        return response
