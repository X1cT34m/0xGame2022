from pwn import *

io = remote('124.223.224.73', 10002)


# 验证码
def proof_of_work():
    rev = io.recvuntil(b"sha256(XXXX+")
    suffix = io.recv(8).decode()
    print(suffix)
    rev = io.recvuntil(b" == ")
    tar = io.recv(64).decode()

    def f(x):
        hashresult = hashlib.sha256(x.encode() + suffix.encode()).hexdigest()
        return hashresult == tar

    prefix = util.iters.mbruteforce(f, string.digits + string.ascii_letters, 4, 'upto')
    io.recvuntil(b'XXXX :')
    io.sendline(prefix.encode())


def exgcd(a, b):
    if b == 0:
        x, y = 1, 0
        return a, x, y
    else:
        d, y, x = exgcd(b, a % b)
        y = y - a // b * x
        return d, x, y


proof_of_work()

io.recvuntil(b"a = ")
a = int(io.recvline()[:-1])
io.recvuntil(b"b = ")
b = int(io.recvline()[:-1])
io.recvuntil(b"c = ")
c = int(io.recvline()[:-1])

_, s, t = exgcd(a, b)
io.recvuntil(b"s = ")
io.sendline(str(s).encode())
io.recvuntil(b"t = ")
io.sendline(str(t).encode())

io.interactive()
