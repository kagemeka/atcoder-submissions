import sys
from math import log2, floor

n, k, *A = map(int, sys.stdin.read().split())

def main():
    if k == 0:
        return sum(A)

    bits = [0] * 40
    for a in A:
        for i in range(40):
            bits[i] += a >> i & 1

    bl = [bits[i] < n / 2 for i in range(40)]

    k_bit = [k >> i & 1 for i in range(40)]
    i = floor(log2(k))
    while True:
        tmp_x = 2 ** i - 1
        x_bit = [tmp_x >> j & 1 for j in range(40)]
        res1 = 0
        res2 = 0
        for j in range(i+1):
            if k_bit[j] & bl[j]:
                res1 += 2 ** j * (n - bits[j])
            else:
                res1 += 2 ** j * bits[j]

            if x_bit[j] & bl[j]:
                res2 += 2 ** j * (n - bits[j])
            else:
                res2 += 2 ** j * bits[j]

        if res2 > res1:
            for j in range(i):
                k_bit[j] |= 1
            k_bit[i] = 0
            break

        for j in range(i-1, -1, -1):
            if k_bit[j] == 1:
                i = j
                break
        else:
            break

    res = 0
    for i in range(40):
        if bl[i] & k_bit[i]:
            res += 2 ** i * (n - bits[i])
        else:
            res += 2 ** i * bits[i]

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
