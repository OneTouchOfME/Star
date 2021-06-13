import socket

s = socket.socket()
print("Socket is created")

s.bind(('localhost', 12345))

s.listen(2)
print('waiting for connection')

while True:

    c, addr=s.accept()
    name=c.recv(1024).decode()
    print(f"adress={addr} and name is {name}")
    c.send(bytes('welcome to socket server side','utf-8'))

    c.close()