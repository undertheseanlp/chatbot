import time
from datetime import datetime

import moment

locale = "Asia/Ho_Chi_Minh"
class TimeUtil:
    @staticmethod
    def timestamp(year, month, day):
        tmp = moment.date(datetime(year, month, day)).locale(locale).date
        timestamp = int(time.mktime(tmp.timetuple()))
        return timestamp

    @staticmethod
    def start_of_day(time_string):
        """
        moment: either HÔM_KIA, HÔM_QUA, HÔM_NAY, NGÀY_MAI, NGÀY_KIA
        """
        today = moment.date(datetime.now()).locale(locale)
        if time_string == "HÔM_KIA":
            day = today.day - 2
        elif time_string == "HÔM_QUA":
            day = today.day - 1
        elif time_string == "HÔM_NAY":
            day = today.day
        elif time_string == "NGÀY_MAI":
            day = today.day + 1
        elif time_string == "NGÀY_KIA":
            day = today.day + 2
        else:
            raise Exception("Cannot resolve time from string {}".format(time_string))
        return TimeUtil.timestamp(today.year, today.month, day)

