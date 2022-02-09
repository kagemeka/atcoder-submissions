import sys
from collections import defaultdict
from string import ascii_lowercase

n, *s = sys.stdin.read().split()
n = int(n)

def main():
    cnt = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        for c in s[i]:
            cnt[i][c] += 1

    for i in range(n - 1):
        for c in ascii_lowercase:
            cnt[i+1][c] = min(cnt[i+1][c], cnt[i][c])
    res = ''
    for v, c in sorted(cnt[-1].items()):
        res += v * c
    print(res)

if __name__ ==  '__main__':
    main()
