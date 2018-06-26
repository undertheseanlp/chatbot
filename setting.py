import os

DIR_PATH_DATA = os.path.dirname(os.path.realpath(__file__)) + "/data"

GREETING_TRAIN_FILE = DIR_PATH_DATA + "/greeting_train_file"

GREETING_FILE = DIR_PATH_DATA + "/greeting"
ORTHER_FILE = DIR_PATH_DATA + "/orther"
WH_WEATHER_FILE = DIR_PATH_DATA + "/wh_weather"
YESNO_WEATHER_FILE = DIR_PATH_DATA + "/yesno_weather"
DIC_WEATHER_FILE = DIR_PATH_DATA + "/dic_weather"
TRAIN_GREETING_FILE = DIR_PATH_DATA + "/train_greeting"
RAW_TRAIN_NER_FILE = DIR_PATH_DATA + "/raw_train_ner"
# TRAIN_NER_FILE = DIR_PATH_DATA + "/train_ner"
NER_CRF_TRAIN_FILE = DIR_PATH_DATA + "/tag.txt"

#==========================================================================

DIR_PATH_MODEL = os.path.dirname(os.path.realpath(__file__)) + "/model"

GREETING_MODEL = DIR_PATH_MODEL + "/model.greeting.pkl"
INTEND_VECTORIZER_MODEL = DIR_PATH_MODEL + "/model.vectorzier.intend.pkl"
INTEND_CLASSIFY_MODEL = DIR_PATH_MODEL + "/model.classify.intend.pkl"
MODEL_NER_FILE = DIR_PATH_MODEL + "/chatbot-ner.ser.gz"
MODEL_NER_CRF_FILE = DIR_PATH_MODEL + "/ner.model"
