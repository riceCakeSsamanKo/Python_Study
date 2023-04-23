from socket import *

server_ip = "127.0.0.1"
server_port = 123

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_ip, server_port))

messages = [
    "GET /example.htm HTTP/1.1\r\n",
    "POST /example.htm HTTP/1.1\r\n",
    "DELETE /example.htm HTTP/1.1\r\n",
]

for message in messages:
    # 메시지 전송
    clientSocket.send(message.encode())
    recvMessage = clientSocket.recv(1024)
    print(f"from Server:{recvMessage.decode()}")

clientSocket.close()
