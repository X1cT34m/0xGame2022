from Crypto.Util.number import *
from hashlib import sha256
from secret import flag
import socketserver
import signal
import string
import random
import os
import gmpy2
import time

table = string.ascii_letters + string.digits
BANNER = br'''
   ___        ____                      ____   ___ ____  ____  
  / _ \__  __/ ___| __ _ _ __ ___   ___|___ \ / _ \___ \|___ \ 
 | | | \ \/ / |  _ / _` | '_ ` _ \ / _ \ __) | | | |__) | __) |
 | |_| |>  <| |_| | (_| | | | | | |  __// __/| |_| / __/ / __/ 
  \___//_/\_\\____|\__,_|_| |_| |_|\___|_____|\___/_____|_____|
  ____                      _   
 | __ )  ___ _______  _   _| |_ 
 |  _ \ / _ \_  / _ \| | | | __|
 | |_) |  __// / (_) | |_| | |_ 
 |____/ \___/___\___/ \__,_|\__|
                                
'''


class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def proof_of_work(self):
        proof = (''.join([random.choice(table) for _ in range(12)])).encode()
        sha = sha256(proof).hexdigest().encode()
        self.send(b"[+] sha256(XXXX+" + proof[4:] + b") == " + sha)
        XXXX = self.recv(prompt=b'[+] Plz Tell Me XXXX :')
        if len(XXXX) != 4 or sha256(XXXX + proof[4:]).hexdigest().encode() != sha:
            return False
        return True

    def get_num(self, bit):
        return random.getrandbits(bit)

    def handle(self):
        signal.alarm(120)
        self.send(BANNER)
        if not self.proof_of_work():
            self.send(b'Oops,you are wrong. Bye~')
            return
        a = self.get_num(16)
        b = self.get_num(16)
        c = gmpy2.gcd(a, b)
        self.send(b"Well, can you tell me a (s,t) that satisfies 'a*s + b*y == c' ?")
        self.send("a = {}".format(a).encode())
        self.send("b = {}".format(b).encode())
        self.send("c = {}".format(c).encode())
        s = int(self.recv(b"s = "))
        t = int(self.recv(b"t = "))
        if a * s + b * t == c:
            self.send(b'Nice!!!!! You solve the problem!!!')
            self.send(flag)
        else:
            self.send(b"Sorry, your answer is wrong~~")
        self.request.close()


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10002
    print("HOST:POST " + HOST + ":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
