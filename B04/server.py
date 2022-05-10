import socket
from euclidean_maths import power_mod

inet = 'localhost'
port = 5000

s = socket.socket()
s.bind((inet, port))
s.listen()
print(f'listening at {inet}:{port}')

c, addr = s.accept()
print(f'connected to {addr}')

e, n = c.recv(1024).decode().split(',')
e = int(e)
n = int(n)
print(f'received public key (e,n): {e,n}')

data = int(input('data: '))
cipher = power_mod(data, e, n)
c.send(f'{cipher}'.encode())
print(f'sent cipher: {cipher}')

s.close()
