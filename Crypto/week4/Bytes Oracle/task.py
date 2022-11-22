import socketserver
from Crypto.Util.number import *
import os
import signal
import string
from random import *
from secret import _flag

banner = r"""                               
  ____        _          ___                 _      
 | __ ) _   _| |_ ___   / _ \ _ __ __ _  ___| | ___ 
 |  _ \| | | | __/ _ \ | | | | '__/ _` |/ __| |/ _ \
 | |_) | |_| | ||  __/ | |_| | | | (_| | (__| |  __/
 |____/ \__, |\__\___|  \___/|_|  \__,_|\___|_|\___|
        |___/                                       

"""
menu = r"""
MENU:
1.GetKey
2.Encrypt
3.Decrypt
4.Quit
"""


def GenerateRSAKey():
    n, phi = 1, 1
    for i in range(4):
        while True:
            p = getPrime(1000)
            if isPrime(p):
                break
        n *= p
        phi *= (p - 1)
    e = getPrime(randint(20, 24))
    d = inverse(e, phi)
    return n, e, d


class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 9182
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def printf(self, msg, newline=True):
        if newline:
            msg += "\n"
        self.request.sendall(msg.encode())

    def scanf(self, prompt='> '):
        self.printf(prompt, newline=False)
        return self._recvall()

    def handle(self):
        signal.alarm(1200)
        self.printf(banner)
        n, e, d = GenerateRSAKey()
        flag = _flag
        flag = bytes_to_long(os.urandom(390) + b"          " + flag.encode() + b"          " + os.urandom(30))
        for ___ in range(1607087):
            self.printf(menu)
            try:
                op = int(self.scanf())
                if op == 1:
                    self.printf(f"n={n}")
                    self.printf(f"e={e}")
                    self.printf(f"c={pow(flag, e, n)}")
                elif op == 2:
                    m = int(self.scanf("Enter your plaintext in decimal format >"))
                    c = pow(m, e, n)
                    msg = long_to_bytes(c).hex()[-2:]
                    self.printf(f"The last byte of your Ciphertext is: {msg}")
                elif op == 3:
                    c = int(self.scanf("Enter your ciphertext in decimal format >"))
                    m = pow(c, d, n)
                    msg = long_to_bytes(m).hex()[-2:]
                    self.printf(f"The last byte of your Plaintext is: {msg}")
                else:
                    break
            except:
                self.printf("Wrong Input")
                break
        self.printf("Quitting...")


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10003
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    print("Server at 0.0.0.0 port " + str(PORT))
    server.serve_forever()
