import socket	
import os 		 
s = socket.socket()		
print ("Socket successfully created")
port = 12345			
s.bind(('', port))		
print ("socket binded to %s" %(port))
s.listen(5)	
print ("socket is listening")	

c, addr = s.accept()	
print ('Got connection from', addr )
c.send('Connection established '.encode())

#*****************************************************************************************************

qq = c.recv(1024).decode().split('\\')[-1]
print('the file name is ',qq)
file_path = 'E:\ABHAY\FUN WITH PYTHON\shared_file'
#*****************************************************************************************************
if os.path.exists(file_path):
    pass
else:
    os.mkdir(file_path)
saved_location = file_path+'\\'+qq

f2 = open(saved_location,'ab')
while True:
    f2.write(c.recv(10000000))
    c.send('ab'.encode())
