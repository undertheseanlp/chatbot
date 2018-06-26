from sklearn.externals import joblib
import setting
import re

class AdapterIntend(object):

    def __init__(self):
        self.vectorizer = joblib.load(setting.INTEND_VECTORIZER_MODEL)
        self.clf = joblib.load(setting.INTEND_CLASSIFY_MODEL)


    def get_intend(self,msg):
        msg = self.format(msg)
        vector = self.vectorizer.transform([msg])
        result = self.clf.predict(vector)
        return result[0]


    def format(self,line):
        fline = re.sub("\?","",line)
        fline = fline.strip()
        return fline

