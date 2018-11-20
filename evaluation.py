import json
from nltk.translate.bleu_score import sentence_bleu
from engine.hoaian import HoaiAn

talks = json.load(open("tests/conversation.json"))

HoaiAn.reply("local", ":build HoaiAn")
HoaiAn.reply("local", ":reset")

count = {
    "talk": 0
}
for talk in talks:
    count["talk"] += 1
    questions = talk["question"]
    answer = talk["answer"][0]
    for question in questions:
        bot_answer = HoaiAn.reply("local", question)
        print(question)
        print(answer)
        print(bot_answer)
        bleu = sentence_bleu([answer.split()], bot_answer.split(), weights=[1, 0, 0, 0])
        print("Bleu: ", bleu)
        print()

print("Count:", count)