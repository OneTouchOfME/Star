import socket

c = socket.socket()
print("Socket is created")

c.connect(('localhost', 12345))
name=input('Enter the name ')
c.send(bytes(name, 'utf-8'))


print(c.recv(1024).decode())