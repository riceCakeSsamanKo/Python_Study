from socket import *
# 서버 정보 (IP, Port)
UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# 소켓 생성 (IPv4, UDP)
sock = socket(AF_INET, SOCK_DGRAM)

# HTTP 요청 메시지 생성
requests = [
    'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n',
    'POST / HTTP/1.1\r\nHost: example.com\r\n\r\n',
    'DELETE / HTTP/1.1\r\nHost: example.com\r\n\r\n',
]

for request in requests:
    # 요청 전송
    sock.sendto(request.encode(), (UDP_IP, UDP_PORT))

    # 응답 수신
    data, serverAddress = sock.recvfrom(1024)

    # 수신한 메시지 출력
    print(f'Received {len(data)} bytes from {serverAddress}:')
    print(data.decode())
