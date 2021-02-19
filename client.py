import socket
import _thread

def receiving(sock):
    while 1:
        msg_out, server = sock.recvfrom(2024)
        print("other>")