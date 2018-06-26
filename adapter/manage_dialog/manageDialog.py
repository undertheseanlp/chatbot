
#Init
def initDialog(request):
    request.session['loc'] = []
    request.session['time'] = []
    request.session['weather'] = []
    request.session['bot_state'] = 1
    request.session['bot_msg'] = ""

#Update
def updateLoc(request,loc):
    request.session['loc'] = loc

def updateTime(request,time):
    request.session['time'] = time

def updateWeather(request,weather):
    request.session['weather'] = weather

def updateState(request,bot_state):
    request.session['bot_state'] = bot_state

def updateMsg(request,bot_msg):
    request.session['bot_msg'] = bot_msg

#Get
def getLoc(request):
    return request.session['loc']

def getTime(request):
    return request.session['time']

def getWeather(request):
    return request.session['weather']

def getState(request):
    return request.session['bot_state']

def getMsg(request):
    return request.session['bot_msg']



