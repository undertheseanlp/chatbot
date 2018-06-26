import datetime
import re

class TimeDetector():

    def __init__(self):
        pass

    def detect_time(self,time):
        data_time = []
        current_time = datetime.datetime.now()
        current_day = current_time.day
        current_month = current_time.month
        current_year = current_time.year
        current_hour = current_time.hour
        current_weekday = current_time.weekday()
        # pattern1 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)giờ'
        # pattern2 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h'
        # pattern3 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)giờ(?:(?:\s*)([0-5]?[0-9])(?:\s*))?'
        # pattern4 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h(?:\s*)([0-5]?[0-9])(?:\s*)'
        pattern5 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9])'
        big_pattern1 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h)(?:\s*)([0-5]?[0-9])(?:\s*)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h)'
        # big_pattern2 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h(?:\s*)([0-5]?[0-9])(?:\s*)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h'
        pattern_spec1 = r'(bình minh|mặt trời mọc)'
        pattern_spec2 = r'(hoàng hôn|chiều tà|mặt trời lặn|chập tối|chiều tối)'
        pattern_spec3 = r'(nửa đêm)'
        pattern_spec4 = r'(về sáng|rạng sáng)'
        pattern_spec5 = r'(đêm xuống|đêm|ban đêm|buổi đêm|khuya)'
        pattern_spec6 = r'(buổi tối|màn đêm buông xuống|tối)'
        pattern_spec7 = r'(ban ngày|buổi ngày)'
        pattern_spec8 = r'(buổi sáng|sáng)'
        pattern_spec9 = r'(buổi chiều|chiều)'
        pattern_spec10 = r'(giữa trưa|buổi trưa|trưa)'
        pattern_spec11 = r'(bây giờ|bây h|hiện tại|lúc này)'

        pattern_spec12 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9]):(?:\s*)(?:[0-5]?[0-9])(?:\s*)(?:sáng|buổi sáng)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h|:)(?:\s*)([0-5]?[0-9])(?:\s*)(?:phút|)(?:\s*)(?:sáng|buổi sáng)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h)(?:\s*)(?:sáng|buổi sáng)'
        pattern_spec13 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9]):(?:\s*)(?:[0-5]?[0-9])(?:\s*)(?:trưa|buổi trưa)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h|:)(?:\s*)([0-5]?[0-9])(?:\s*)(?:phút|)(?:\s*)(?:trưa|buổi trưa)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h)(?:\s*)(?:trưa|buổi trưa)'
        pattern_spec14 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9]):(?:\s*)(?:[0-5]?[0-9])(?:\s*)(?:chiều|buổi chiều)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h|:)(?:\s*)([0-5]?[0-9])(?:\s*)(?:phút|)(?:\s*)(?:chiều|buổi chiều)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h)(?:\s*)(?:chiều|buổi chiều)'
        pattern_spec15 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9]):(?:\s*)(?:[0-5]?[0-9])(?:\s*)(?:tối|buổi tối|đêm|khuya)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h|:)(?:\s*)([0-5]?[0-9])(?:\s*)(?:phút|)(?:\s*)(?:tối|buổi tối|đêm|khuya)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)(?:giờ|h)(?:\s*)(?:tối|buổi tối|đêm|khuya)'


        bol = False
        patterns = re.findall(pattern_spec12,time)
        if len(patterns) == 0:
            patterns = re.findall(pattern_spec4, time)
            if len(patterns) == 0:
                patterns = re.findall(pattern_spec8, time)
                for pattern in patterns:
                    for i in range(6,11):
                        sub_time = {
                            "hour": str(i),
                            "minute": "00"
                        }
                        data_time.append(sub_time)
            else :
                for pattern in patterns:
                    for i in range(4,7):
                        sub_time = {
                            "hour": str(i),
                            "minute": "00"
                        }
                        data_time.append(sub_time)
        else :
            bol = True
            for pattern in patterns:
                if pattern[4] != "" :
                    sub_time = {
                        "hour": pattern[4],
                        "minute": "00"
                    }
                elif pattern[2]!="" :
                    sub_time = {
                        "hour": pattern[2],
                        "minute": pattern[3]
                    }
                else :
                    sub_time = {
                        "hour": pattern[0],
                        "minute": pattern[1]
                    }
                data_time.append(sub_time)

        patterns = re.findall(pattern_spec13, time)
        if len(patterns) == 0:
            patterns = re.findall(pattern_spec10, time)
            for pattern in patterns:
                for i in range(11,13):
                    sub_time = {
                        "hour": str(i),
                        "minute": "00"
                    }
                    data_time.append(sub_time)
        else :
            bol = True
            for pattern in patterns:
                if pattern[4] != "":
                    sub_time = {
                        "hour": pattern[4],
                        "minute": "00"
                    }
                elif pattern[2]!="":
                    sub_time = {
                        "hour": pattern[2],
                        "minute": pattern[3]
                    }
                else :
                    sub_time = {
                        "hour": pattern[0],
                        "minute": pattern[1]
                    }
                data_time.append(sub_time)

        patterns = re.findall(pattern_spec14, time)
        if len(patterns) == 0:
            patterns = re.findall(pattern_spec9, time)
            for pattern in patterns:
                for i in range(13, 18):
                    sub_time = {
                        "hour": str(i),
                        "minute": "00"
                    }
                    data_time.append(sub_time)
        else :
            bol = True
            for pattern in patterns:
                if pattern[4] != "":
                    if int(pattern[4]) < 12 :
                        hour = 12 + int(pattern[4])
                    else :
                        hour = pattern[4]
                    sub_time = {
                        "hour": str(hour),
                        "minute": "00"
                    }
                elif pattern[2]!="":
                    if int(pattern[2]) < 12 :
                        hour = 12 + int(pattern[2])
                    else :
                        hour = pattern[2]
                    sub_time = {
                        "hour": str(hour),
                        "minute": pattern[3]
                    }
                else :
                    if int(pattern[0]) < 12 :
                        hour = 12 + int(pattern[0])
                    else :
                        hour = pattern[0]
                    sub_time = {
                        "hour": str(hour),
                        "minute": pattern[1]
                    }
                data_time.append(sub_time)

        patterns = re.findall(pattern_spec15, time)
        if len(patterns) == 0:
            patterns = re.findall(pattern_spec6, time)
            if len(patterns) == 0 :
                patterns = re.findall(pattern_spec3, time)
                if len(patterns) != 0:
                    sub_time = {
                        "hour": "0",
                        "minute": "00"
                    }
                    data_time.append(sub_time)
                else :
                    patterns = re.findall(pattern_spec5, time)
                    for pattern in patterns :
                        for i in range(18, 25):
                            sub_time = {
                                "hour": str(i % 24),
                                "minute": "00"
                            }
                            data_time.append(sub_time)
                        for i in range(1, 5):
                            sub_time = {
                                "hour": str(i),
                                "minute": "00"
                            }
                            data_time.append(sub_time)
            else :
                for pattern in patterns:
                    for i in range(18, 25):
                        sub_time = {
                            "hour": str(i%24),
                            "minute": "00"
                        }
                        data_time.append(sub_time)
        else :
            bol = True
            print(patterns)
            for pattern in patterns:
                if pattern[4] != "":
                    if int(pattern[4]) <= 12 and int(pattern[4])>=6:
                        hour = (12 + int(pattern[4]))%24
                    else :
                        hour = pattern[4]
                    sub_time = {
                        "hour": str(hour),
                        "minute": "00"
                    }
                elif pattern[2]!="":
                    if int(pattern[2])<=12 and int(pattern[2])>=6:
                        hour = (12 + int(pattern[2]))%24
                    else :
                        hour = pattern[2]
                    sub_time = {
                        "hour": str(hour),
                        "minute": pattern[3]
                    }
                else :
                    if int(pattern[0])<=12 and int(pattern[0])>=6:
                        hour = (12 + int(pattern[0]))%24
                    else :
                        hour = pattern[0]
                    sub_time = {
                        "hour": str(hour),
                        "minute": pattern[1]
                    }
                data_time.append(sub_time)
        if not bol :
            patterns = re.findall(big_pattern1, time)
            for pattern in patterns:
                if pattern[2] != "" :
                    sub_time = {
                        "hour": pattern[2],
                        "minute": "00"
                    }
                else :
                    sub_time = {
                        "hour": pattern[0],
                        "minute": pattern[1]
                    }
                data_time.append(sub_time)
            patterns = re.findall(pattern5, time)
            for pattern in patterns:
                sub_time = {
                    "hour": pattern[0],
                    "minute": pattern[1]
                }
                data_time.append(sub_time)

        patterns = re.findall(pattern_spec1,time)
        for pattern in patterns:
            for i in range(5,7):
                sub_time = {
                    "hour": str(i),
                    "minute": "00"
                }
                data_time.append(sub_time)
        patterns = re.findall(pattern_spec2, time)
        for pattern in patterns:
            for i in range(5, 7):
                sub_time = {
                    "hour": str(i),
                    "minute": "00"
                }
                data_time.append(sub_time)
        patterns = re.findall(pattern_spec7, time)
        for pattern in patterns:
            for i in range(6,18):
                sub_time = {
                    "hour": str(i),
                    "minute": "00"
                }
                data_time.append(sub_time)
        patterns = re.findall(pattern_spec11, time)
        for pattern in patterns:
            sub_time = {
                "hour": str(current_time.hour),
                "minute": str(current_time.minute)
            }
            data_time.append(sub_time)

        if len(data_time) == 0 :
            data_time.append({
                "hour": None,
                "minute": None
            })
        return data_time


    def _detect_range(self):
        pass

    def _detect_return_date(self):
        pass

if __name__ == "__main__" :
    timeDetector = TimeDetector()
    # msg = "tôi sẽ đi làm vào 12 giờ bình minh, 9giờ , 11:3:4 và 19 giờ 56 ,còn ngày mai lúc 20h06  hoặc lúc 23 h 09 có ca nhạc đêm khuya"
    msg = "7:23:45 sáng"
    data = timeDetector.detect_time(msg)
    # print(len(data))
    for i in data :
        print(i)