import socket

server = "example.org"
port = 1234          # 80
message = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
s.sendall(bytes(message.format(server), 'utf8'))

while True:
    data = s.recv(512)
    if not data: break
    print(str(data, 'utf8'))

s.close()
