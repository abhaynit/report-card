import socket			
s = socket.socket()		
port = 12345			
s.connect(('127.0.0.1', port))

print('enter the file location to send',end = ' ')
#file_location = input()
file_location = 'ak.mp4'
print("SERVER : ",s.recv(10000000).decode())
s.send(file_location.encode())

with open(file_location, "rb") as f:
    while True:
        byte = f.read(10000000)
        if not byte:
            s.send(''.encode())
            break
        s.send(byte)
        s.recv(10000000).decode() 