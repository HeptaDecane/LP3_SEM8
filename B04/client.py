import math
import socket
from euclidean_maths import power_mod


def compute_public_key(phi):
    """
        1 < e < phi
        and,
        gcd(e,phi) = 1
    """
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e

    raise Exception(f'e does not exist for given phi: {phi}')


def compute_private_key(e, phi):
    """
        e*d % phi = 1
        therefore,
        d = (phi*i +1) / e
        if (phi*i + 1) % e == 0
    """
    i = 1
    while True:
        if (phi*i + 1) % e == 0:
            break
        i += 1

    d = (phi*i +1) / e
    return int(d)


p = int(input('prime number (p): '))
q = int(input('prime number (q): '))

n = p*q
phi = (p-1)*(q-1)

e = compute_public_key(phi)
d = compute_private_key(e, phi)

print(f'public key (e,n): {e,n}')
print(f'private key (d,n): {d,n}')

inet = 'localhost'
port = 5000

s = socket.socket()
s.connect((inet, port))

s.send(f'{e},{n}'.encode())
print(f'sent public key (e,n): {e,n}')

cipher = int(s.recv(1024).decode())
print(f'received cipher: {cipher}')

data = power_mod(cipher, d, n)
print(f'data: {data}')

s.close()
