from socket import *

# server 이름(ip)와 포트 번호를 알고 있어야 연결 가능
serverName = '127.0.0.1'
serverPort = 12000

# 소켓 생성
clientSocket = socket(AF_INET, SOCK_STREAM)
# 서버 소켓에 TCP 커넥션 연결
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase message:')

# 비트로 부호화 해서 전송
clientSocket.send(message.encode())
# 서버에서 반환된 데이터
modifiedMessage = clientSocket.recv(1024)

print('From Server:', modifiedMessage.decode())
clientSocket.close()
