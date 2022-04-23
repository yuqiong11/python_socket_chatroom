import socket
import time
import pickle



HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5050))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} established.")

    # msg = "Welcome to the server"
    d = {1:"HE", 2:"IS"}
    l = [1,2,3,45,6]
    msg = pickle.dumps(l)
    # print(msg)

    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg

    clientsocket.send(msg)

    # while True:
    #     time.sleep(3)
    #     msg = f"Time is {time.asctime( time.localtime(time.time()) )}"
    #     msg = f"{len(msg):<{HEADER_SIZE}}" + msg

    #     clientsocket.send(bytes(msg, "utf-8"))