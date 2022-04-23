import socket
import pickle

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5050))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(20)
        if new_msg:
            print(f"new msg length: {msg[:HEADER_SIZE]}")
            msg_len = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADER_SIZE == msg_len:
            print("full message received on client")
            print(full_msg[HEADER_SIZE:])

            d = pickle.loads(full_msg[HEADER_SIZE:])
            print(d)
            new_msg = True
            full_msg = b''

