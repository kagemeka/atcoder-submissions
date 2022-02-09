import sys
from itertools import chain

n, k, *a = map(int, sys.stdin.read().split())
*a, = map(lambda x: min(k, x), a)
# bitsが大きくなりすぎないように前処理
a.sort()

mask = (1 << k) - 1
def is_needed(i):
    res = 1
    for j in chain(a[:i], a[i+1:]):
        res |= res << j
        res &= mask
    return res >> (k - a[i])

def main():
    # neededとなるindexの最小を求める
    lo = 0 # 可能最小
    hi = n # 可能最大 + 1
    while lo != hi:
        i = (lo + hi) // 2
        if is_needed(i):
            hi = i
        else:
            lo = i + 1

    return hi

if __name__ == '__main__':
    ans = main()
    print(ans)
