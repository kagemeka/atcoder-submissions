import sys
from collections import defaultdict

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

    ans = 0
    for k, v in res.items():
        if k <= 2:
            ans += v
        else:
            ans += v * (k - 1)
    print(ans)

if __name__ == '__main__':
    main()
