from Crypto.Util.number import *

a = 27
b = 121

f = open("cipher.txt", "rb")
s = f.read()
flag = ""
a_ = inverse(a, 128)
for i in s:
    tmp = (i - b) * a_ % 128
    flag += chr(tmp)

print(flag)
