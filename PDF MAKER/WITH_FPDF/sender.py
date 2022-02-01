from socket import *
import time
 
# Assigning server IP and server port
serverName = "127.0.0.1"
serverPort = 5000
# Setting buffer length
buffer_length = 500
# Assigning the audio file a name
my_audio_file = r"E:\django\boot\testapp\static\audio\a.mp3"
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Opening the audio file
f = open(my_audio_file, "rb")
# Reading the buffer length in data
data = f.read(buffer_length)

# While loop for the transfer of file
while data:
    if clientSocket.sendto(data, (serverName, serverPort)):
        data = f.read(buffer_length)
        time.sleep(0.02)  # waiting for 0.02 seconds
clientSocket.close()
f.close()
print("File has been Transferred")