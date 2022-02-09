import sys
from itertools import product
from string import digits

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    cand = list(''.join(p) for p in product(digits, repeat=3))

    res = set()
    for c in cand:
        i = s.find(c[0])
        if i == -1:
            continue
        j = s.find(c[1], i+1)
        if j == -1:
            continue
        k = s.find(c[2], j+1)
        if k == -1:
            continue

        res.add(c)

    ans = len(res)
    print(ans)

if __name__ == '__main__':
    main()
