import json
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from engine.hoaian import HoaiAn
import numpy as np


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
        answer = talk["answer"][0]
        for question in questions:
            count["question"] += 1
            bot_answer = HoaiAn.reply("local", question)
            if not bot_answer:
                bot_answer = ""
            bleu = sentence_bleu([answer.lower().split()], bot_answer.lower().split(), smoothing_function=SmoothingFunction().method4)
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
