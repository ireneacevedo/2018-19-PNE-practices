
import socket
from Seq import Seq

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 8089
    IP = '212.128.253.82'

    s.connect((IP, PORT))

    sequence = input('Please enter a sequence: ')
    sequence = sequence.upper()
    sequence_1 = Seq(sequence)
    sequence_2 = Seq.reverse(sequence_1)
    sequence_3 = Seq.complement(sequence_2)
    sending = sequence_3.strbases
    s.send(str.encode(sending))

    msg = s.recv(2048).decode('utf-8')

    s.close()

