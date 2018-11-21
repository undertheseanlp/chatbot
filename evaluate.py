import json
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from engine.hoaian import HoaiAn
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def scoring(question, answers):
    bot_answer = HoaiAn.reply("local", question)
    if len(answers) == 0:
        answer = ""
        return 0, bot_answer, answer
    bleus = [(answer, sentence_bleu([bot_answer.lower().split()], answer.lower().split(), weights=[1, 0, 0, 0])) for answer in answers]
    answer, bleu = max(bleus, key=lambda x: x[1])
    return bleu, bot_answer, answer


def evaluate(filepath):
    talks = json.load(open(filepath))
    count = {
        "talk": 0,
        "question": 0
    }
    scores = []
    for talk in talks:
        count["talk"] += 1
        questions = talk["question"]
        for question in questions:
            count["question"] += 1
            bleu, bot_answer, answer = scoring(question, talk["answer"])
            scores.append(bleu)
            if bleu < 0.8:
                print("\nQuestion :", question)
                print("Correct  :", answer)
                print("Actual   :", bot_answer)
                print("Bleu     : ", bleu)
                print()
    print("Count:", count)
    print("Score:", np.mean(scores))


HoaiAn.reply("local", ":build HoaiAn")
HoaiAn.reply("local", ":reset")
HoaiAn.reply("local", ":trace")

files = [
    "data/hoaian01/raw/conversation.json",
    "data/hoaian01/raw/myself.json"
]
for filepath in files:
    print("")
    print(filepath)
    evaluate(filepath)
