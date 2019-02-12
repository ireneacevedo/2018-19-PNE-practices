
# Creating a chat
import socket
PORT = 8080
IP = '212.128.253.64'

while True:
    msg = input('Enter a message:')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))
    s.send(str.encode(msg))

msg1 = s.recv(2048).decode('utf-8')
print('MESSAGE FROM THE SERVER:')
print(msg)

s.close()

print('The end')

