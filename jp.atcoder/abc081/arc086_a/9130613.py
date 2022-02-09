import sys
from collections import Counter

n, k, *a = map(int, sys.stdin.read().split())

def main():
    c = Counter(a)
    l = len(c)
    if l <= k:
        return 0

    c = sorted(c.items(), key=lambda x: x[1])
    res = 0
    for i in range(l - k):
        res += c[i][1]

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
