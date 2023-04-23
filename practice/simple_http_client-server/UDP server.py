from socket import *

# 서버 정보 (IP, Port)
UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# 소켓 생성 (IPv4, UDP)
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    # 클라이언트로부터 데이터 수신
    data, clientAddress = sock.recvfrom(1024)

    # 수신한 메시지 크기 출력
    print(f'Received {len(data)} bytes from {clientAddress}')

    # 수신한 메시지 파싱
    lines = data.decode('ascii').split('\r\n')
    method, path, _ = lines[0].split()

    # HTTP 메소드에 따른 응답 생성
    if method == 'GET':
        response = 'HTTP/0.1 200 OK\r\n'
    elif method == 'POST':
        response = 'HTTP/0.1 404 Not Found\r\n\r\n'
    else:
        response = 'HTTP/0.1 400 Bad Request\r\n\r\n'

    # 응답 전송
    sock.sendto(response.encode(), clientAddress)
