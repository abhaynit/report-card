import socket			
s = socket.socket()		
port = 12345			
s.connect(('127.0.0.1', port))
while True:
    print ("Server : ",s.recv(1024).decode())
    ab = input("YOU : ")
    s.send(ab.encode())