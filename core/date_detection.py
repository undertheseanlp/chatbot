import datetime
import re

class DateDetector():

    def __init__(self):
         pass

    def detect_date(self,date):
        data_date = []
        current_time = datetime.datetime.now()
        current_day = current_time.day
        current_month = current_time.month
        current_year = current_time.year
        current_weekday = current_time.weekday()
        pattern1 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])'
        # pattern2 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)tháng(?:\s*)(1[0-2]|0?[1-9])'
        pattern3 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)tháng(?:\s*)(1[0-2]|0?[1-9])(?:\s*)năm(?:\s*)(2[0-9]{3})'
        pattern4 = r'(?:[^0-9\w]|^)tháng(?:\s*)(1[0-2]|0?[1-9])(?:\s*)năm(?:\s*)(2[0-9]{3})'
        pattern5 = r'(?:[^0-9\w]|^)tháng(?:\s*)(1[0-2]|0?[1-9])'
        pattern6 = r'(?:[^0-9\w]|^)năm(?:\s*)(2[0-9]{3})'
        pattern7 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:[/-]|tháng)(?:\s*)(1[0-2]|0?[1-9])'
        pattern8 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:[/-]|tháng)(?:\s*)(1[0-2]|0?[1-9])(?:\s*)(?:[/-]|năm)(?:\s*)(2[0-9]{3})'
        pattern9 = r'(?:[^0-9\w]|^)(1[0-2]|0?[1-9])(?:\s*)(?:[/-]|năm)(?:\s*)(2[0-9]{3})'
        pattern_spec1 = r'(hôm nay|bây giờ|bây h|hiện tại|hiện nay|lúc này|nay)'
        pattern_spec2 = r'(ngày mai|mai|hôm sau)'
        pattern_spec3 = r'(ngày kia|ngày mốt|hôm kia)'
        pattern_spec4 = r'(ngày kia nữa|hôm kia nữa)'
        pattern_spec5 = r'(hôm qua)'
        pattern_spec6 = r'(hôm trước)'
        pattern_spec7 = r'(tuần này|tuần hiện tại|tuần hiện giờ)'
        pattern_spec8 = r'(tuần sau|tuần tới)'
        pattern_spec9 = r'(tuần kia|tuần sau nữa)'
        pattern_spec10 = r'(tuần trước|tuần vừa rồi)'
        pattern_spec11 = r'(thứ 2|thứ hai)'
        pattern_spec12 = r'(thứ 3|thứ ba)'
        pattern_spec13 = r'(thứ 4|thứ tư)'
        pattern_spec14 = r'(thứ 5|thứ năm)'
        pattern_spec15 = r'(thứ 6|thứ sáu)'
        pattern_spec16 = r'(thứ 7|thứ bảy)'
        pattern_spec17 = r'(chủ nhật)'

        pattern_spec19 = r'(tháng sau)'
        pattern_spec20 = r'(tháng trước)'
        pattern_spec21 = r'(tháng này|tháng hiện tại)'
        pattern_spec22 = r'(năm sau)'
        pattern_spec23 = r'(năm này)'
        pattern_spec24 = r'(năm trước)'
        pattern_spec25 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:tháng sau)'
        pattern_spec26 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:tháng trước)'
        pattern_spec27 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:tháng này|tháng hiện tại)'

        pattern_spec28 = r'(vài ngày tới|vài ngày nữa|vài hôm nữa|vài hôm tới)'
        pattern_spec29 = r'(vài ngày trước|vài ngày vừa rồi|vài ngày vừa qua|vài ngày qua|vài hôm trước|vài hôm vừa rồi)'

        pattern_spec30 = r'(?:[^0-9\w]|^)(\d+)(?:\s*)(?:ngày tới|ngày nữa|hôm nữa|hôm tới)'
        pattern_spec31 = r'(?:[^0-9\w]|^)(\d+)(?:\s*)(?:vài ngày trước|vài ngày vừa rồi|vài ngày vừa qua|vài ngày qua|vài hôm trước|vài hôm vừa rồi)'


        patterns = re.findall(pattern1, date)
        for pattern in patterns:
            sub_date = {
                "day": pattern,
                "month": None,
                "year": None
            }
            data_date.append(sub_date)
        # patterns = re.findall(pattern2, date)
        # for pattern in patterns:
        #     sub_date = {
        #         "day": pattern[0],
        #         "month": pattern[1],
        #         "year": None
        #     }
        #     data_date.append(sub_date)
        patterns = re.findall(pattern3, date)
        for pattern in patterns:
            sub_date = {
                "day": pattern[0],
                "month": pattern[1],
                "year": pattern[2]
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern4, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": pattern[0],
                "year": pattern[1]
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern5, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": pattern,
                "year": None
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern6, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": None,
                "year": pattern
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern7, date)
        for pattern in patterns:
            sub_date = {
                "day": pattern[0],
                "month": pattern[1],
                "year": None
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern8, date)
        for pattern in patterns:
            sub_date = {
                "day": pattern[0],
                "month": pattern[1],
                "year": pattern[2]
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern9, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": pattern[0],
                "year": pattern[1]
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec1, date)
        for pattern in patterns:
            sub_date = {
                "current" : True,
                "day": str(current_day),
                "month": str(current_month),
                "year": str(current_year)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec2, date)
        fu_day = current_time + datetime.timedelta(1)
        for pattern in patterns:
            sub_date = {
                "day": str(fu_day.day),
                "month": str(fu_day.month),
                "year": str(fu_day.year)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec3, date)
        fu_day = current_time + datetime.timedelta(2)
        for pattern in patterns:
            sub_date = {
                "day": str(fu_day.day),
                "month": str(fu_day.month),
                "year": str(fu_day.year)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec4, date)
        fu_day = current_time + datetime.timedelta(3)
        for pattern in patterns:
            sub_date = {
                "day": str(fu_day.day),
                "month": str(fu_day.month),
                "year": str(fu_day.year)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec5, date)
        fu_day = current_time - datetime.timedelta(1)
        for pattern in patterns:
            sub_date = {
                "day": str(fu_day.day),
                "month": str(fu_day.month),
                "year": str(fu_day.year)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec6, date)
        fu_day = current_time - datetime.timedelta(2)
        for pattern in patterns:
            sub_date = {
                "day": str(fu_day.day),
                "month": str(fu_day.month),
                "year": str(fu_day.year)
            }
            data_date.append(sub_date)
        # =======================================================
        data_day_week = []
        data_week = []
        patterns = re.findall(pattern_spec7, date)
        for pattern in patterns:
            sub_date = {
                "week": 0
            }
            data_week.append(sub_date)
        patterns = re.findall(pattern_spec8, date)
        for pattern in patterns:
            sub_date = {
                "week": 1
            }
            data_week.append(sub_date)
        patterns = re.findall(pattern_spec9, date)
        for pattern in patterns:
            sub_date = {
                "week": 2
            }
            data_week.append(sub_date)
        patterns = re.findall(pattern_spec10, date)
        for pattern in patterns:
            sub_date = {
                "week": -1
            }
            data_week.append(sub_date)
        patterns = re.findall(pattern_spec11,date)
        for pattern in patterns:
            sub_date = {
                "day" : 0
            }
            data_day_week.append(sub_date)
        patterns = re.findall(pattern_spec12, date)
        for pattern in patterns:
            sub_date = {
                "day": 1
            }
            data_day_week.append(sub_date)
        patterns = re.findall(pattern_spec13, date)
        for pattern in patterns:
            sub_date = {
                "day": 2
            }
            data_day_week.append(sub_date)
        patterns = re.findall(pattern_spec14, date)
        for pattern in patterns:
            sub_date = {
                "day": 3
            }
            data_day_week.append(sub_date)
        patterns = re.findall(pattern_spec15, date)
        for pattern in patterns:
            sub_date = {
                "day": 4
            }
            data_day_week.append(sub_date)
        patterns = re.findall(pattern_spec16, date)
        for pattern in patterns:
            sub_date = {
                "day": 5
            }
            data_day_week.append(sub_date)
        patterns = re.findall(pattern_spec17, date)
        for pattern in patterns:
            sub_date = {
                "day": 6
            }
            data_day_week.append(sub_date)

        data_date2 = []
        if len(data_week) == 0 and len(data_day_week) > 0:
            data_week.append({
                "week" : 0
            })
        for i in data_week:
            dc = i['week'] * 7
            if len(data_day_week) == 0 :
                for j in range(7):
                    d = dc + j - current_weekday
                    fu_day = current_time + datetime.timedelta(d)
                    sub_date = {
                        "day": fu_day.day,
                        "month": fu_day.month,
                        "year": fu_day.year
                    }
                    data_date2.append(sub_date)

            else :
                for j in data_day_week:
                    d = dc + j['day'] - current_weekday
                    fu_day = current_time + datetime.timedelta(d)
                    sub_date = {
                        "day": fu_day.day,
                        "month": fu_day.month,
                        "year": fu_day.year
                    }
                    data_date2.append(sub_date)

        # =======================================================

        patterns = re.findall(pattern_spec19, date)
        for pattern in patterns:
            if current_month == 12 :
                sub_date = {
                    "day": None,
                    "month": str(1),
                    "year": None
                }
            else:
                sub_date = {
                    "day": None,
                    "month": str(current_month + 1),
                    "year": None
                }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec20, date)
        for pattern in patterns:
            if current_month == 1:
                sub_date = {
                    "day": None,
                    "month": str(12),
                    "year": None
                }
            else:
                sub_date = {
                    "day": None,
                    "month": str(current_month - 1),
                    "year": None
                }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec21, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": str(current_month),
                "year": None
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec22, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": None,
                "year": str(current_time.year + 1)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec23, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": None,
                "year": str(current_time.year)
            }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec24, date)
        for pattern in patterns:
            sub_date = {
                "day": None,
                "month": None,
                "year": str(current_time.year - 1)
            }
            data_date.append(sub_date)
        # =======================================================
        patterns = re.findall(pattern_spec25, date)
        for pattern in patterns:
            if current_month == 12:
                sub_date = {
                    "day": pattern,
                    "month": str(1),
                    "year": None
                }
            else:
                sub_date = {
                    "day": pattern,
                    "month": str(current_month + 1),
                    "year": None
                }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec26, date)
        for pattern in patterns:
            if current_month == 1:
                sub_date = {
                    "day": pattern,
                    "month": str(12),
                    "year": None
                }
            else:
                sub_date = {
                    "day": pattern,
                    "month": str(current_month - 1),
                    "year": None
                }
            data_date.append(sub_date)
        patterns = re.findall(pattern_spec27, date)
        for pattern in patterns:
            sub_date = {
                "day": pattern,
                "month": str(current_month),
                "year": None
            }
            data_date.append(sub_date)
        # =======================================================
        patterns = re.findall(pattern_spec28, date)
        for pattern in patterns:
            for i in range(3):
                fu_day = current_time + datetime.timedelta(i + 1)
                data_date.append({
                    "day": str(fu_day.day),
                    "month": str(fu_day.month),
                    "year": str(fu_day.year)
                })
        patterns = re.findall(pattern_spec29, date)
        for pattern in patterns:
            for i in range(3):
                fu_day = current_time + datetime.timedelta(0-i-1)
                data_date.append({
                    "day": str(fu_day.day),
                    "month": str(fu_day.month),
                    "year": str(fu_day.year)
                })

        patterns = re.findall(pattern_spec30, date)
        for pattern in patterns:
            for i in range(1,int(pattern)+1):
                fu_day = current_time + datetime.timedelta(i)
                data_date.append({
                    "day": str(fu_day.day),
                    "month": str(fu_day.month),
                    "year": str(fu_day.year)
                })

        patterns = re.findall(pattern_spec31, date)
        for pattern in patterns:
            for i in range(1, int(pattern) + 1):
                fu_day = current_time - datetime.timedelta(i)
                data_date.append({
                    "day": str(fu_day.day),
                    "month": str(fu_day.month),
                    "year": str(fu_day.year)
                })

        data_date = self.filter_date(data_date)
        data_date = data_date + data_date2
        if len(data_date) == 0 :
            data_date.append({
                "day": None,
                "month": None,
                "year": None
            })
        return data_date


    def unique_date(self,data):
        pass


    def _detect_range(self):
        pass

    def _detect_return_date(self):
        pass

    def filter_date(self,data_date):
        data = []
        data_tmp = []
        data_tmp1 = []
        data_tmp2 = []
        data_tmp3 = []
        data_tmp4 = []
        data_tmp5 = []
        data_tmp6 = []
        for date in data_date:
            if 'current' in date :
                data.append(date)
                continue
            if date['day'] != None and date['month'] == None and date['year'] == None:
                data_tmp1.append(date)
            if date['day'] == None and date['month'] != None and date['year'] == None:
                data_tmp2.append(date)
            if date['day'] == None and date['month'] == None and date['year'] != None:
                data_tmp3.append(date)
            if date['day'] != None and date['month'] != None and date['year'] == None:
                data_tmp4.append(date)
            if date['day'] == None and date['month'] != None and date['year'] != None:
                data_tmp5.append(date)
            if date['day'] != None and date['month'] != None and date['year'] != None:
                data_tmp6.append(date)
        data_tmp.extend(data_tmp6)
        if len(data_tmp6) == 0 :
            data_tmp.extend(data_tmp4)
            data_tmp.extend(data_tmp5)
        else :
            data_tmp_cp4 = data_tmp4.copy()
            for i in data_tmp4 :
                for j in data_tmp6:
                    if i['day']==j['day'] and i['month']==j['month'] :
                        data_tmp_cp4.remove(i)
                        break
            data_tmp_cp5 = data_tmp5.copy()
            for i in data_tmp5 :
                for j in data_tmp6:
                    if i['month']==j['month'] and i['year']==j['year'] :
                        data_tmp_cp5.remove(i)
                        break
            data_tmp.extend(data_tmp_cp4)
            data_tmp.extend(data_tmp_cp5)
        data.extend(data_tmp)
        if len(data_tmp) == 0 :
            data.extend(data_tmp1)
            data.extend(data_tmp2)
            data.extend(data_tmp3)
        else :
            data_tmp_cp1 = data_tmp1.copy()
            for i in data_tmp1:
                for j in data_tmp:
                    if i['day'] == j['day']:
                        data_tmp_cp1.remove(i)
                        break
            data_tmp_cp2 = data_tmp2.copy()
            for i in data_tmp2:
                for j in data_tmp:
                    if i['month'] == j['month']:
                        data_tmp_cp2.remove(i)
                        break
            data_tmp_cp3 = data_tmp3.copy()
            for i in data_tmp3:
                for j in data_tmp:
                    if i['year'] == j['year']:
                        data_tmp_cp3.remove(i)
                        break
            data.extend(data_tmp_cp1)
            data.extend(data_tmp_cp2)
            data.extend(data_tmp_cp3)
        return data

if __name__ == "__main__" :
    dateDetector = DateDetector()
    # msg = "ngày 20/1 có lịch hẹn ,ngày 18/9/2017 , tháng 4 và 5-4 hoặc 12-4-2021 sẽ như thế nào hay hôm qua hoặc bây giờ ?"
    # msg = "tháng 1 năm 2017 và năm 2016"
    # msg = "ngày mai và hôm qua ,hiện tại, đến ngày 24 tháng 6/2011 có gì ,ngày 8 tháng 9"
    # msg = " ngày 19 tháng này thứ 7 tuần này"
    msg = " ngày kia nữa"
    data = dateDetector.detect_date(msg)
    print("=========================")
    for i in data:
        print(i)

