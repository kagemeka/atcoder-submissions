import sys

import sys
sys.setrecursionlimit(10**6)
table = dict()
def choose(n, r, mod=None): # no mod, or mod ≠ prime
    if r > n or r < 0: return 0
    if r == 0: return 1
    if (n, r) in table: return table[(n, r)]
    table[(n, r)] = (choose(n - 1, r) + choose(n - 1, r - 1))
    return table[(n,r)]

n, *a = map(int, sys.stdin.read().split())
a += [0]

def main():
    prev = 1001001001
    cnt = 0
    res = 0
    for x in a:
        if x <= prev:
            res += choose(cnt, 2) + cnt
            cnt = 1
        else:
            cnt += 1
        prev = x
    print(res)

if __name__ ==  '__main__':
    main()
