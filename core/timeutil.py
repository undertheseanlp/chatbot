import time
from datetime import datetime

import moment


class TimeUtil:
    @staticmethod
    def timestamp(year, month, date):
        tmp = moment.date(datetime(year, month, date)).locale("Asia/Ho_Chi_Minh").date
        timestamp = int(time.mktime(tmp.timetuple()))
        return timestamp
