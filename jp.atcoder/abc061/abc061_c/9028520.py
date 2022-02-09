import sys
from collections import defaultdict

n, k, *ab = map(int, sys.stdin.read().split())
ab = zip(*[iter(ab)] * 2)

def main():
    cnt = defaultdict(int)
    for a, b in ab:
        cnt[a] += b

    s = 0
    for v, c in sorted(cnt.items()):
        s += c
        if s >= k:
            return v

if __name__ == '__main__':
    ans = main()
    print(ans)
