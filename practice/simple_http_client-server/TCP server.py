from socket import *

server_ip = "127.0.0.1"
server_port = 123

# 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', server_port))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    clientMessage = connectionSocket.recv(2048)
    print(f"received message: {clientMessage}")
    message = clientMessage.decode('ascii').split("\r\n")

    method, path, _ = message[0].split()

    if method == "GET":
        response = "HTTP/0.1 200 OK"
    elif method == "POST":
        response = "HTTP/0.1 404 Not Found"
    else:
        response = "HTTP/0.1 400 Bad Request"
    connectionSocket.send(response.encode())
