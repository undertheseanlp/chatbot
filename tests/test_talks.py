from engine.hoaian import HoaiAn
from engine.hungcuong import HungCuong

turn = "hungcuong"
message = "hi"
count = 0
while count < 100:
    if turn == "hoaian":
        message = HoaiAn.reply("hungcuong", message)
        turn = "hungcuong"
    else:
        message = HungCuong.reply("hoaian", message)
        turn = "hoaian"
    count += 1
    print("{}>".format(turn), message)