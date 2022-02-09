import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
*A, = map(int, sys.stdin.readline().split())
BC = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    res = defaultdict(int)
    for a in A:
        res[a] += 1

    for b, c in BC:
        res[c] += b

    ans = 0
    r = n
    for v, c in sorted(res.items(), reverse=True):
        if c <= r:
            r -= c
            ans += v * c
        else:
            ans += v * r
            break

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
