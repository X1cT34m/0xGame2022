import random

x = [random.getrandbits(32) for _ in range(32)]

# flag为0xGame{md5(sum(x))}

for i in range(32):
    ans = 0
    rand = [random.getrandbits(32) for _ in range(32)]
    for j in range(31):
        ans += x[j] * rand[j]
        print("x{} * {} + ".format(j, rand[j]), end="")
    ans += x[31] * rand[31]
    print("x{} * {} = ".format(31, rand[31]), end="")
    print(ans)
