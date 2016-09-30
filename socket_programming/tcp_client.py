import socket

host = '10.20.6.25'
port = 7000

socket = socket.socket()
socket.connect((host, port))

while True:
    msg_for_server = input('Enter message for server> ')
    socket.send(msg_for_server.encode())
    msg_from_server = socket.recv(1024).decode()
    print('server says> ', str(msg_from_server))

socket.close()
