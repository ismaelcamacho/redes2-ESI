import socket
import _thread

def receiving(sock):
    while 1:
        msg_in, peer = sock.recvfrom(1024)
        print("other> {}".format(msg_in.decode()))
        if msg_in == b"bye":
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 12345))

_thread.start_new_thread(receiving, (sock,))

while 1:
    msg_out = input()
    sock.sendto(msg_out.encode(), peer)
    if msg_out == "bye":
        break
    