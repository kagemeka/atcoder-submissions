import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
sp = [sys.stdin.readline().split() for _ in range(n)]

def main():
    res = defaultdict(list)
    for i in range(n):
        s, p = sp[i]
        res[s].append((int(p), i+1))

    for s, l in sorted(res.items()):
        for p, i in sorted(l, reverse=True):
            yield i

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
