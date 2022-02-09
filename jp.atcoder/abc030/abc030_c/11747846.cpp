import sys
from bisect import bisect_left as bi_l

n, m, x, y, *ab = map(int, sys.stdin.read().split())
a, b = ab[:n], ab[n:]

def main():
    t = cnt = 0
    while True:
        try: t = a[bi_l(a, t)] + x
        except: break
        try: t = b[bi_l(b, t)] + y
        except: break
        cnt += 1
    print(cnt)

if __name__ ==  '__main__':
    main()
