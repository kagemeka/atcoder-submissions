import sys
from collections import Counter

n, *v = map(int, sys.stdin.read().split())

def main():
    c1 = sorted(Counter(v[::2]).items(), key=lambda x: -x[1])
    c2 = sorted(Counter(v[1::2]).items(), key=lambda x: -x[1])
    if c1[0][0] != c2[0][0]: res = n - c1[0][1] - c2[0][1]
    else:
        if len(c1) > len(c2): c1, c2 = c2, c1
        if len(c2) == 1: res = n // 2
        else:
            if len(c1) == 1: res = n - c1[0][1] - c2[1][1]
            else:
                res = n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1])
    print(res)

if __name__ ==  '__main__':
    main()
