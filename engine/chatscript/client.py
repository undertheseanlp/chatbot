# Simple chat client to communicate with chat script server
# Not very efficient, since it uses a thread per socket model,
# If servicing a large number of clients, twisted may be a better fit

from optparse import OptionParser
import socket
import sys


def sendAndReceiveChatScript(text, server='127.0.0.1', port=1024, timeout=10):
    try:
        # Connect, send, receive and close socket. Connections are not persistent
        text = "talk"
        msgToSend = u'%s\u0000%s\u0000%s\u0000' % (user, botname, text)
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
            msg = msg + chunk.decode("utf-8")
        s.close()
        return msg
    except Exception as e:
        print(e)
        return None


def main():
    server = "127.0.0.1"
    port = 1024
    botname = "HOAIAN"

    # Setup the command line arguments.
    optp = OptionParser()

    # user name to login to chat script as
    optp.add_option("-u", dest="user", help="user id, required")
    # botname
    optp.add_option("-b", dest="botname", help="which bot to talk to, if not specified, will use default bot")
    # server
    optp.add_option("-s", dest="server", help="chat server host name (default is " + str(server) + ")")
    # port
    optp.add_option("-p", dest="port", help="chat server listen port (default is " + str(port) + ")")

    opts, args = optp.parse_args()

    if opts.user is None:
        optp.print_help()
        sys.exit(1)
    user = opts.user

    if opts.botname is not None:
        botname = opts.botname

    if opts.server is not None:
        server = opts.server

    if opts.port is not None:
        port = int(opts.port)

    print("Hi " + user + ", enter ':quit' to end this session")

    while True:
        s = input("[" + user + "]" + ">: ").lower().strip()
        if s == ':quit':
            break

        # Ensure empty strings are padded with atleast one space before sending to the
        # server, as per the required protocol
        if s == "":
            s = " "
        # Send this to the server and print the response
        # Put in null terminations as required
        msg = u'%s\u0000%s\u0000%s\u0000' % (user, botname, s)
        msg = str.encode(msg)
        resp = sendAndReceiveChatScript(msg, server=server, port=port)
        if resp is None:
            print("Error communicating with Chat Server")
            break  # Stop on any error
        else:
            print("[Bot]: " + resp)

if __name__ == '__main__':
    server = "127.0.0.1"
    port = 1024

    user = "anhv"
    botname = "Hoaian"

    resp = sendAndReceiveChatScript("talk", server=server, port=port)
    print(resp)