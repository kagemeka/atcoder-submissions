import sys
from collections import defaultdict
from math import ceil

def main():
    n, *p = map(int, sys.stdin.read().split())
    p = [None] + p
    res = defaultdict(int)
    cnt = 0
    for i in range(1, n + 1):
        if p[i] == i:
            cnt += 1
        else:
            if cnt >= 1:
                res[cnt] += 1
                cnt = 0
    res[cnt] += 1

    ans = 0
    for k, v in res.items():
        ans += v * ceil(k / 2)
    print(ans)

if __name__ == '__main__':
    main()
