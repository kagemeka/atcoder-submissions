# 2019-11-22 22:30:40(JST)
import sys
import itertools

def main():
    n, m = map(int, sys.stdin.readline().split())
    lrs = map(int, sys.stdin.read().split())
    *lrs, = zip(lrs, lrs, lrs)

    total = sum(s for l, r, s in lrs)
    res = [0 for _ in range(m+2)]
    res[0] = 0

    for l, r, s in lrs:
        res[l] += s
        res[r+1] -= s


    res =  list(itertools.accumulate(res))
    res.pop(0); res.pop()

    ans = total - min(res)
    print(ans)
# editorial より いもす法
if __name__ == '__main__':
    main()
