import sys
from collections import defaultdict

cnt = defaultdict(int)

def main():
    n, *a = map(int, sys.stdin.read().split())
    a.sort()
    l = a[0]
    r = a[-1]

    for val in a:
        cnt[val] += 1

    ans = 0
    for i in range(l, r+1):
        ans = max(ans, cnt[i-1] + cnt[i] + cnt[i+1])

    print(ans)

if __name__ == '__main__':
    main()
