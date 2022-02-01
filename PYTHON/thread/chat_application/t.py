import socket
import _thread
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080
new_socket.bind((host_name, port))
print("BINDED SUCCESSFULLY")
print("This is server IP: ", s_ip)
new_socket.listen(20)

def clientthread(conn, addr):
    while(True):
        message = input('Me : ')
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(client, ':', message)

while True:
    conn, addr = new_socket.accept()
    print (addr[0] + " connected")
    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')
    bc = "CHAT GROUP"
    conn.send(bc.encode())
    #clientthread(conn,addr)
    _thread.start_new_thread(clientthread,(conn,addr))    