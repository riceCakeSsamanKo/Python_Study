from socket import *

# 포트 번호 12000
serverPort = 12000
# TCP 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
# 서버 소켓 bind
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # connectionSocket == serverSocket들 중 clientSocket과 연결된 소켓
    connectionSocket, clientAddress = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    capitalizedMessage = message.upper()
    connectionSocket.send(capitalizedMessage.encode())
    connectionSocket.close()

