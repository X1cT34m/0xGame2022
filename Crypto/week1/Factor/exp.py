from Crypto.Util.number import *

c = 49549088434190402681586345733724247189
p = 9735957770491659841
q = 18254685097880877413
n = p * q
phi = (p - 1) * (q - 1)
e = 0x10001
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
