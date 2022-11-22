from secret import flag
import random
import gmpy2


def gen_key():
    while True:
        x = random.randint(1, 128)
        if gmpy2.gcd(x, 128) == 1:
            break
    y = random.randint(1, 128)
    return x, y


cipher = ""
a, b = gen_key()
for i in flag:
    tmp = (ord(i) * a + b) % 128
    cipher += chr(tmp)

with open("cipher.txt", "w") as f:
    f.write(cipher)

with open("key.txt", "w") as f:
    f.write("a = {}".format(str(a)))
    f.write("\n")
    f.write("b = {}".format(str(b)))
