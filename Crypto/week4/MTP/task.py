from secret import flag


def str_xor(m, k):
    return ''.join([chr(m[i] ^ k[i]) for i in range(len(m))])


m = []
c = []
l = len(flag)
with open('m.txt', 'rb') as f:
    tmp = f.read(l)
    while tmp:
        m.append(tmp)
        c.append(str_xor(tmp, flag))
        tmp = f.read(l)
with open('output.txt', 'w') as f:
    for i in c:
        f.write(i.encode().hex().ljust(2 * l, 'f') + '\n')
