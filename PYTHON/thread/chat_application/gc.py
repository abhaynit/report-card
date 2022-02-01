# Python program to implement client side of chat room.
import socket
import select
import sys
import random
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
Port = 8080
server.connect((s_ip, Port))
 
while True:
    """
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    """

    abc = [1,2]
    t = random.choice(abc)
    print(t)
    if t == 1:
        server.send("hey say something".encode())
        message = server.recv(2048)
        pt = message.decode()
        print (pt)
    else:
        message = sys.stdin.readline()
        server.send(message.encode())
        print ("<You>" + message)
server.close()