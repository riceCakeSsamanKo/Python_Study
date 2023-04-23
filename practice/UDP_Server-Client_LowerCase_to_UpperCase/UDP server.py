from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 서버 소켓 bind
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("-- message response --")
