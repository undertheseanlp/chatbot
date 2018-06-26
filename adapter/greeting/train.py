from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.externals import joblib
import setting
import re
import random


def read_file(filePath):
    with open(filePath,"r") as file:
        data = file.readlines()
    data2 = []
    for line in data:
        dline = format(line)
        if dline != "":
            data2.append(dline)
    return data2


def load_data(raw_data):
    data = {}
    for i in range(len(raw_data)):
        if i%2==0:
            line = raw_data[i]
            line2 = raw_data[i+1]
            keys = line.split("|")
            values = line2.split("|")
            for i in keys:
                i = i.strip()
                if i!="":
                    data[i] = values
        else:
            continue
    return data


def train(data):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(data)
    joblib.dump(vectorizer, setting.GREETING_MODEL)
    return vectorizer


def format(line):
    fline = re.sub("\?","",line)
    fline = fline.strip()
    return fline


def main():
    filePath = setting.GREETING_TRAIN_FILE
    data = load_data(read_file(filePath))
    keys = []
    keys.extend(data.keys())
    vectorizer = train(data.keys())
    vectorizer = joblib.load(setting.GREETING_MODEL)
    while True :
        msg = input("human : ")
        msg = format(msg)
        if msg == "":
            print("bot : bạn nhập tin nhắn đi !")
        else :
            result = best_response(msg,data,vectorizer)
            print(result)
            print("\n")


def best_response(msg,data,vectorizer):
    min = 1000
    msg = vectorizer.transform([msg])
    value = None
    for i in data:
        ti = vectorizer.transform([i])
        a = euclidean_distances(ti[0],msg[0])
        if min > a[0][0]:
            value = i
            min = a[0][0]
    print(value)
    print(min)
    if value == None:
        return "khong hieu"

    values = data[value]
    id = random.randint(0,len(values)-1)

    return data[value][id]


if __name__ =="__main__":
    main()
    # a =read_file(setting.GREETING_TRAIN_FILE)
    # for i in a :
    #     print(i)