import random
from engine.translator import Translator


def brain(bot):
    print(bot._var["name"], ":")
    uid = bot.current_user()
    facts = bot.get_uservar(uid, "facts")
    if len(facts) > 0:
        print("Facts ->", list(facts))
        fact = random.choice(list(facts))
        facts.remove(fact)
        bot.set_uservar(uid, "facts", facts)
        command = "seek {}".format(fact)
        print(command)
        text = Translator.run(command)
        text += "{" + "topic=seek_{}".format(fact.replace(" ", "_")) + "}"
    else:
        print("Facts -> empty")
        text = "..."
    return text
