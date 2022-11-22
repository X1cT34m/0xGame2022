from pwn import*
from Crypto.Util.number import*
io=remote("0.0.0.0", 10009)
io.recvuntil(b"4.Quit\n")
io.sendline(b"1")
io.recvuntil(b"n=")
n=int(io.recvline())
io.recvuntil(b"e=")
e=int(io.recvline())
io.recvuntil(b"c=")
c=int(io.recvline())
l,r=0,n
t=1
n_ = n % 256
submap = {}
for i in range(0, 256):
	submap[-n_ * i % 256] = i
while l<r:
	if t%30==0:
		print(t,r-l)
	d=(r-l)//256
	io.recvuntil(b">")
	io.sendline(b"3")
	io.recvuntil(b">")
	io.sendline(str(pow(256,t*e%n,n)*c%n).encode())
	io.recvuntil(b": ")
	k = submap[int(io.recvline(),16)]
	l, r = l + k*d, l + (k+1)*d
	t = t+1
print(long_to_bytes(l))
io.interactive()