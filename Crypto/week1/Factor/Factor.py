from Crypto.Util.number import *
from secret import flag

m = bytes_to_long(flag)
n = 177726843226591634556244030635816071333
assert m < n
e = 0x10001
c = pow(m, e, n)

print(c)

# 49549088434190402681586345733724247189
