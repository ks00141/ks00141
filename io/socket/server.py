import socket           #socket module import

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # 파일과 비슷하게 추상화된 구조체가 생성 되는듯
                                                            # 파일처럼 우리는 추상화된 구조체에 데이터를 쓰고
                                                            # 물리적인 전송을 구조체가 해주는듯
                                                            # AF_INET = 
server.bind(('',9999))

server.listen()

client_socket, addr = server.accept()


while True:
    data = client_socket.recv(1024)

    if data:
        print(data.decode())
    if data.decode() == 'end':
        break

client_socket.close()
server.close()
