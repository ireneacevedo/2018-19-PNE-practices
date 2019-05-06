from seq3 import Seq
import socket

PORT = 8080
IP = '255.255.255.0'
MAX_OPEN_REQUEST = 5

def operation(s, cs):
    """Performs the operations we are asked"""
    msg = cs.recv(2048).decode('utf-8')
    msg = msg.partition('\n')
    sequence = msg[0].upper()
    seq = Seq(sequence)
    names_operations = msg[2].split('\n')
    check = 'ACGT'

    if msg[0] == ' ':
        result = 'ALIVE'

    elif not (msg[0].upper().strip(check) == ''):
        result = 'ERROR'
    else:
        result = 'OK'

    if result == 'ALIVE' or result == 'ERROR':
        return result
    else:
        operations = {'len': seq.len(),
                     'complement': seq.complement(),
                     'reverse': seq.reverse(),
                     'countA': seq.count('A'),
                   'countC': seq.count('C'),
                     'countT': seq.count('T'),
                     'countG': seq.count('G'),
                     'percA': seq.perc('A'),
                   'percC': seq.perc('C'),
                     'percT': seq.perc('T'),
                     'percG': seq.perc('G')}

        sol = '{}\nThe sequence is: {}\n'.format(result, seq.strbases)
        for i in names_operations:
            for name in operations.keys():
                if i == name:
                    sol += str(operations[name]) + '\n'
        return sol


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(MAX_OPEN_REQUEST)

while True:
    print('waiting for connections at : {}, {}'.format(IP, PORT))
    (client_socket, address) = s.accept()

    print("CONNECTION From the IP: {}".format(address))

    msg = operation(s, client_socket)

    info = str.encode(msg)
    client_socket.send(info)
    print('Message sent')
    client_socket.close()