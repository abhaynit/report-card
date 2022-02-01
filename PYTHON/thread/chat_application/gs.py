import socket
import select
import sys
import _thread
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
Port = 8080
server.bind((s_ip, Port))
server.listen(100)
list_of_clients = []

def clientthread(conn,addr):
    mes = "welcome to this chatroom"
    conn.send(mes.encode())
    while(True):
        try:
            message = conn.recv(2048)
            mt = message.decode()
            if mt == "hey say something":
                print(message.decode()) 
                server.send("hi how are you ".encode())
            if len(mt)>0 and mt!="hey say something" :
                print("<" + addr[0] + ">" + message)
                message_to_send = "<" + addr[0] + ">" + message
                broadcast(message_to_send,conn)


            else:
                remove(conn) 
        except:
            continue

 

def broadcast(message, connection):
	for clients in list_of_clients:
		if clients!=connection:
			try:
				clients.send(message)
			except:
				clients.close()

				# if the link is broken, we remove the client
				remove(clients)

def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

while True:
	conn, addr = server.accept()
	list_of_clients.append(conn)
	print (addr[0] + " connected")
	_thread.start_new_thread(clientthread,(conn,addr))	
