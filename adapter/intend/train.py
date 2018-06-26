import os
import re

import setting
from sklearn.svm import SVC,LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib


def create_train_file_yesno_weather(filePath):
    data = []
    with open(filePath,"r") as file:
        lines = file.readlines()
    for line in lines:
        if(line.strip() == ""):
            continue
        else:
            data.append(line.strip())
    data2 = []
    for d in data:
        d2 = re.sub("trời","thời tiết",d)
        data2.append(d2)
    with open(filePath,"a") as file:
        for d in data2:
            file.writelines("\n")
            file.writelines(d)


def create_train_file_wh_weather(filePath):
    data = []
    with open(filePath, "r") as file:
        lines = file.readlines()
    for line in lines:
        if (line.strip() == ""):
            continue
        else:
            data.append(line.strip())
    data2 = []
    for d in data:
        if("như thế nào" in d):
            d2 = re.sub("như thế nào", "ra sao", d)
            data2.append(d2)
    with open(filePath, "a") as file:
        for d in data2:
            file.writelines("\n")
            file.writelines(d)


def train():
    train_data,train_labels = load_data_train()
    vectorizer = TfidfVectorizer(ngram_range=(1,6))
    vectorizer.fit(train_data)
    train_data = vectorizer.transform(train_data)
    # clf = SVC(kernel='poly', degree=4, gamma=1, C=100)
    clf = LinearSVC()
    clf.fit(train_data, train_labels)
    # a = vectorizer.transform(["thời tiết mai mưa không"])
    # b = clf.predict(a)
    # print(b)
    joblib.dump(vectorizer,setting.INTEND_VECTORIZER_MODEL)
    joblib.dump(clf,setting.INTEND_CLASSIFY_MODEL)
    return vectorizer,clf


def load_data_train():
    list_file_path = [setting.GREETING_FILE,setting.WH_WEATHER_FILE,setting.YESNO_WEATHER_FILE,setting.ORTHER_FILE]
    data = []
    labels = []
    for filePath in list_file_path:
        if filePath == setting.GREETING_FILE:
            read_file(filePath,data,labels,label=1)
        elif filePath == setting.WH_WEATHER_FILE:
            read_file(filePath,data,labels,label=2)
        elif filePath == setting.YESNO_WEATHER_FILE:
            read_file(filePath,data,labels,label=3)
        else:
            read_file(filePath,data,labels,label=4)
    return data,labels


def read_file(filePath,data,labels,label):
    with open(filePath,"r") as file:
        lines = file.readlines()
    for line in lines:
        fline = format(line)
        if(fline!="") :
            data.append(fline)
            labels.append(label)


def format(line):
    fline = re.sub("\?","",line)
    fline = fline.strip()
    return fline


def classify(msg):
    return "hello"


def main():
    vectorizer, clf = train()
    while True :
        msg = input("human : ")
        msg = format(msg)
        vector = vectorizer.transform([msg])
        result = clf.predict(vector)
        if msg == "":
            print("bot : bạn nhập tin nhắn đi !")
        else :
            response = classify(msg)
            print("bot : {}".format(result[0]))


if __name__ == "__main__":
    main()

