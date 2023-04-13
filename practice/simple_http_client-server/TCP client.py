import socket

# 서버 정보 (IP, Port)
UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# 소켓 생성 (IPv4, UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# HTTP 요청 메시지 생성
requests = [
    b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n',
    b'POST / HTTP/1.1\r\nHost: example.com\r\n\r\n',
    b'DELETE / HTTP/1.1\r\nHost: example.com\r\n\r\n',
]

for req in requests:
    # 요청 전송
    sock.sendto(req, (UDP_IP, UDP_PORT))

    # 응답 수신
    data, addr = sock.recvfrom(1024)

    # 수신한 메시지 출력
    print(f'Received {len(data)} bytes from {addr}:')
    print(data.decode('ascii'))
