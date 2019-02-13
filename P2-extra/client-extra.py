import socket
from Seq import Seq

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 8094
    IP = '212.128.253.82'

    s.connect((IP, PORT))

    sequence_1 = input('Please enter a sequence: ')
    sequence_1 = sequence_1.upper()

    s.send(str.encode(sequence_1))

    msg = s.recv(2048).decode('utf-8')

    print(msg)
    s.close()