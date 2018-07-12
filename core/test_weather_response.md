| function | input  | expect outcome |
|----| ------------- | ------------- |
| weather_api()| time, loc, weather (tách từ input của user)  | response trả về cho người dùng  |
|convert_time()| time dạng text (VD : ngày mai)  | cụ thể ngày, tháng, năm (VD : 3/7/2018) |
| detect_location()| loc dạng text (VD : Hà Nội) | cụ thể lat, long của loc|
|fill_time()| time rõ ngày, tháng, năm | time đầy đủ nếu output của convert_time() thiếu|
|query_api()| dict của time rõ ngày, tháng, năm, loc dạng lat long, kiểu thời tiết | kết quả từ api weather trả về|
|filter_msg()| data : thông tin trả về từ api, weather, loc, time : tách từ input user| tách 1 số thông tin cần thiết từ kết quả trả về của api|
|response_msg()| filter_msg : thông tin từ api đã được lọc bớt từ filter_msg(), weather, time : tách từ input user| sinh ra câu trả lời cho user| 