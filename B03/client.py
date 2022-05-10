import socket

inet = 'localhost'
port = 5000


s = socket.socket()
s.connect((inet, port))

p = int(input('prime number (p): '))
q = int(input('prime number (q): '))

s.send(f'{p},{q}'.encode())
print(f'sent (p,q): {p,q}')

b = int(input('private key (b): '))
s0 = (q ** b) % p

r0 = int(s.recv(1024).decode())
s.send(f'{s0}'.encode())
print(f'exchanged (R,S): {r0, s0}')

s1 = (r0 ** b) % p
r1 = int(s.recv(1024).decode())
s.send(f'{s1}'.encode())
print(f'exchanged (Rk,Sk): {r1, s1}')

print('success' if r1 == s1 else 'failure')
