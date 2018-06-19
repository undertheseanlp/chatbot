import random
from engine.translator import Translator


def brain(bot):
    uid = bot.current_user()
    print("Current user: ", uid)
    facts = bot.get_uservar(uid, "facts")
    if len(facts) > 0:
        fact = random.choice(list(facts))
        facts.remove(fact)
        bot.set_uservar(uid, "facts", facts)
        command = "seek {}".format(fact)
        print(command)
        text = Translator.run(command)
        text += "{" + "topic=seek_{}".format(fact.replace(" ", "_")) + "}"
    else:
        text = "..."
    return text
