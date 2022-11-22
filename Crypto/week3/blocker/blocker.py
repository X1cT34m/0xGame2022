from Crypto.Util.number import *
import random
from secret import flag

a = random.getrandbits(32)
b = random.getrandbits(32)


def circular_shift_left(int_value, k, bit=32):
    bin_value = bin(int_value)[2:].zfill(32)
    bin_value = bin_value[k:] + bin_value[:k]
    int_value = int(bin_value, 2)
    return int_value


def enc_block(block):
    block = bytes_to_long(block)
    block ^= a
    block = circular_shift_left(block, 11)
    block ^= b
    return block


def enc_msg(msg):
    block_length = 4
    msg = msg + ((block_length - len(msg) % block_length) % block_length) * b'\x00'
    plain_block = [msg[block_length * i: block_length * (i + 1)] for i in range(len(msg) // block_length)]
    cipher = b""
    IV = bytes_to_long(b"0xgm")
    for block in plain_block:
        c = enc_block(block) ^ IV
        IV = c
        cipher += long_to_bytes(c)
    return cipher


print("a =", a)
print("b =", b)
print("cipher =", enc_msg(flag))

'''
a = 232825750
b = 1828860569
cipher = b'\x9a]\xec\x18\xd9\x98\x1d\x85\x0b}V\xf0\xc9\x98\x8d\x85"<\xf4\x02+\xa1m\xe7\xa0\xa6dJ\x8b\x93u?\x0b\x8d\xf62'
'''
