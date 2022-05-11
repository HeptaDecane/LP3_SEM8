import socket

inet = 'localhost'
port = 5000


s = socket.socket()
s.bind((inet, port))
s.listen()
print(f'listening at {inet}:{port}')

c, addr = s.accept()
print(f'connected to {addr}')

p, q = c.recv(1024).decode().split(',')
p = int(p)
q = int(q)
print(f'received (p,q): {p, q}')

a = int(input('private key (a): '))
r0 = (q ** a) % p

c.send(f'{r0}'.encode())
s0 = int(c.recv(1024).decode())
print(f'exchanged (R,S): {r0, s0}')

r1 = (s0 ** a) % p
c.send(f'{r1}'.encode())
s1 = int(c.recv(1024).decode())
print(f'exchanged (Rk,Sk): {r1, s1}')

print('success' if r1 == s1 else 'failure')

s.close()
