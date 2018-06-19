from engine.hoaian import HoaiAn
from engine.hungcuong import HungCuong
from util import sync_engine

turn = "hungcuong"
message = "command start"
count = 0
while count < 100:
    if turn == "hoaian":
        message = HoaiAn.reply("hungcuong", message)
        print("{:10s}>".format(turn), message)
        turn = "hungcuong"
    else:
        message = HungCuong.reply("hoaian", message)
        print("{:10s}>".format(turn), message)
        turn = "hoaian"
    count += 1
