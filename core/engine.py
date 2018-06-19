import random
from engine.translator import Translator


def brain(bot):
    # fact = random.choice(list(THINGS))
    # THINGS.remove(fact)
    fact = "user name"
    command = "seek {}".format(fact)
    print(command)
    text = Translator.run(command)
    text += "{" + "topic=seek_{}".format(fact.replace(" ", "_")) + "}"
    return text
