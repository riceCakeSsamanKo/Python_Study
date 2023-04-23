from socket import *

serverName = '127.0.0.1'
serverPort = 12000
# UDP 소켓 생성
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')

# connection이 개설되지 않았으므로 sendto 함수에 서버 주소와 포트넘버를 명시해서 보낼 위치 알려줌
clientSocket.sendto(message.encode(), (serverName, serverPort))

# 서버에서 반환된 데이터
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()
