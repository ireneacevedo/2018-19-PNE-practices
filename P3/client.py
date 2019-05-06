import socket

# SERVER IP, PORT
IP = '255.255.255.0'
PORT = 8080

while True:

    #ask for the string
    msg = input('Enter a sequence and the operations separated by commas: ')
    if msg != '':
        msg = msg.replace(',', '\n')
        msg = msg.replace(' ', '')
    else:
        msg = ' '

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()