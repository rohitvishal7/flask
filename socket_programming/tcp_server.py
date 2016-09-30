import socket

host = '10.20.6.25'
port = 7000

socket = socket.socket()
socket.bind((host, port))
print('TCP server started on port 7000.. waiting for clients!!\n')
socket.listen(1)
conn, addr = socket.accept()
print('Client request received: ', str(addr))
while True:
    msg_from_client = conn.recv(1024).decode()
    print('client says> ', str(msg_from_client))
    msg_for_client = input('Enter message for client> ')
    conn.send(msg_for_client.encode())

socket.close()
