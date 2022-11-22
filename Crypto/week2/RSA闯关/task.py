from Crypto.Util.number import *
from secret import flag, hint

# part1
print('part1:')
m = bytes_to_long(flag)
p = getPrime(512)
q = getPrime(512)
n = p * q
e = 5
c = pow(m, e, n)
print(f'n = {n}')

# part2
print('part2:')
m = c
while True:
    p = getPrime(256)
    q = 2 * p - 1
    if isPrime(q):
        break
r = getPrime(256)
n = (p ** 2) * (q ** 3) * r
q = 2 * p - 1
r = n // p // p // q // q // q
phi = p * (p - 1) * (q ** 2) * (q - 1) * (r - 1)
e = 0x10001
c = pow(m, e, n)
e = 0x10001
d = inverse(e, phi)
print(f'p = {p}')
print(f'n = {n}')

# part3
print('part3:')
m = c
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 0x10001
c = pow(m, e, n)
print(f'n1 = {n}')
m_hint = bytes_to_long(hint)
p = getPrime(1024)
n = p * q
e = 0x10001
c_hint = pow(m_hint, e, n)
print(f'n2 = {n}')
print(f"c_hint = {c_hint}")

# part4
print('part4:')
m = c
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e1 = 823
e2 = 827
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f'n = {n}')
