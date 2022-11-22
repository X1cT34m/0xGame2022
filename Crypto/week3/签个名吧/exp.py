from hashlib import *
from Crypto.Util.number import *

s0 = 1155391566683353144613828381835889947132557976718
s1 = 182166581822791423481695372664923137176789829383
q = 1427665647738374763020227949129429759446792665193
m0 = b'0xGame'
m1 = b'hack_fun'
hm0 = bytes_to_long(sha256(m0).digest())
hm1 = bytes_to_long(sha256(m1).digest())
k = (inverse(s1 - s0, q) * (hm1 - hm0)) % q
# print(k)
r0 = 9569108440001628337054549116871993930089020799
x = inverse(r0, q) * (s0 * k - hm0) % q
# print(x)
flag = '0xGame{' + md5(str(x).encode()).hexdigest() + '}'
print(flag)
