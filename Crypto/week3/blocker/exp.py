from Crypto.Util.number import *

a = 232825750
b = 1828860569
cipher = b'\x9a]\xec\x18\xd9\x98\x1d\x85\x0b}V\xf0\xc9\x98\x8d\x85"<\xf4\x02+\xa1m\xe7\xa0\xa6dJ\x8b\x93u?\x0b\x8d\xf62'
block_length = 4


def circular_shift_left(int_value, k, bit=32):
    bin_value = bin(int_value)[2:].zfill(32)
    bin_value = bin_value[k:] + bin_value[:k]
    int_value = int(bin_value, 2)
    return int_value


def dec_block(block):
    block ^= b
    block = circular_shift_left(block, 21)
    block ^= a
    block = long_to_bytes(block)
    return block


ff = []
flag = b""
plain_block = [cipher[block_length * i: block_length * (i + 1)] for i in range(len(cipher) // block_length)]

flag += (dec_block(bytes_to_long(b'0xgm') ^ bytes_to_long(plain_block[0])))
for i in range(8):
    flag += (dec_block(bytes_to_long(plain_block[i]) ^ bytes_to_long(plain_block[i + 1])))
print(flag)
