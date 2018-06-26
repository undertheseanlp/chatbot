import pycrfsuite
import setting
from pyvi.pyvi import ViTokenizer, ViPosTagger

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

def detect_entity(question):
    text = ViPosTagger.postagging(ViTokenizer.tokenize(question))
    detect = []
    ar = []
    for i in range(len(text[0])):
        l = []
        l.append(text[0][i])
        l.append(text[1][i])
        ar.append(tuple(l))
    detect.append(ar)
    X_detect = [sent2features(s) for s in detect]
    tagger = pycrfsuite.Tagger()
    tagger.open(setting.MODEL_NER_CRF_FILE)
    y_detect = [tagger.tag(xseq) for xseq in X_detect]
    pred = []
    for i in range(len(detect[0])):
        k = detect[0][i][0]
        k = k.replace("_", " ")
        v = y_detect[0][i]
        kv = []
        kv.append(k)
        kv.append(v)
        pred.append(tuple(kv))
    return pred

def get_weather(list_entity):
    wet = []
    for i in range(len(list_entity)):
        if list_entity[i][1] == "WET":
            wet.append(list_entity[i][0])
    return wet
