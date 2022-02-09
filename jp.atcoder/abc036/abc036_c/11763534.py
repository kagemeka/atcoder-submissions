import sys
from collections import defaultdict

n, *a = map(int, sys.stdin.read().split())

def main():
    res = defaultdict(list)
    for i in range(n):
        res[a[i]].append(i)
    queue = [res[k] for k in sorted(res)]
    b = [None] * n
    v = 0
    for q in queue:
        for i in q:
            b[i] = v
        v += 1
    print(*b, sep='\n')

if __name__ ==  '__main__':
    main()
