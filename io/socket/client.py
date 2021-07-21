import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('192.168.56.1',9999))
while True:
    data = input('send : ')
    client.sendall(data.encode())
    if data == 'end':
        break
