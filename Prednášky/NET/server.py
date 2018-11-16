import socket
from datetime import datetime

html = """
<html>
<head>
    <meta charset="utf-8"/>
    <title>Webstránka</title>
</head>
<body>
  <h1>Ahoj</h1>
</body>
</html>"""


response = ("HTTP/1.1 200 OK\n"
            "Server: My-Simple-Server\n"
            "Date: {}\n"
            "Content-Type: Content-Type: text/html; charset=utf-8\n"
            "Content-Length: {}\n"
            "Connection: close\n\n")

host = ''
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(3)

while True:
    client, address = s.accept()

    print("Connected by: {}".format(address))
    data = client.recv(512)
    #print(str(data, 'utf8'))

    time = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    html = open('index.html', 'r').read()
    l = len(bytes(html, 'utf8'))

    client.send(bytes(response.format(time, l) + html, 'utf8'))
    client.close()

s.close()
