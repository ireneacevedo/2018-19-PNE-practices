import socket

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 8086
    IP = "212.128.253.82"

    s.connect((IP, PORT))
    msg = input('Enter a message:')
    s.send(str.encode(msg))

    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER:')
    print(msg)

    s.close()
