import socket

defaultUser = "anhv"


def sendAndReceiveChatScript(text, user=defaultUser, server='127.0.0.1', port=1024, timeout=10):
    try:
        botname = "hoaian"
        msgToSend = '%s\u0000%s\u0000%s\u0000' % (user, botname, text)
        msgToSend = str.encode(msgToSend)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)  # timeout in secs
        s.connect((server, port))
        s.sendall(msgToSend)
        msg = ''
        while True:
            chunk = s.recv(1024)
            if chunk == b'':
                break
            msg = msg + chunk.decode("utf-8", errors="ignore")
        s.close()
        return msg
    except Exception as e:
        print(e)
        return None


class HoaiAn:
    @staticmethod
    def reply(text, user=defaultUser):
        server = "127.0.0.1"
        port = 1024
        response = sendAndReceiveChatScript(text, user, server=server, port=port)
        return response

    @staticmethod
    def init():
        server = "127.0.0.1"
        port = 1024
        sendAndReceiveChatScript(":reset", server=server, port=port)


if __name__ == '__main__':
    HoaiAn.init()
    response = HoaiAn.reply("mấy tuổi", user="test2")
    print(response)
