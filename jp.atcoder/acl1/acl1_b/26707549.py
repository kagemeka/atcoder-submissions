import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def calc_div(N):
    sq = int(N**.5 + 10)
    x = np.arange(1, sq)
    x = x[N % x == 0]
    x = np.concatenate((x, N // x))
    return np.unique(x)

def inv_mod(a, mod):
    b, u, v = mod, 1, 0
    while b:
        t = a // b
        a, b = b, a - t * b
        u, v = v, u - t * v
    return u % mod

def main(N):
    N *= 2
    div = calc_div(N)
    for a in div:
        a = int(a)
        b = N // a
        if np.gcd(a, b) != 1:
            continue
        # b | an + 1
        n = (-inv_mod(a, b)) % b
        k = a * n
        if k == 0:
            k += N
        assert k * (k + 1) % N == 0
        yield k

N = int(read())
print(min(main(N)))
