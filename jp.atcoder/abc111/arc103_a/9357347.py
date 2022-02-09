import sys
from collections import Counter

n, *v = map(int, sys.stdin.read().split())

def main():
    c1 = sorted(Counter(v[::2]).items(), reverse=True, key=lambda x: x[1])
    c2 = sorted(Counter(v[1::2]).items(), reverse=True, key=lambda x: x[1])

    if c1[0][0] != c2[0][0]:
        return n // 2 - c1[0][1] + n // 2 - c2[0][1]
    else:
        if len(c1) == len(c2) == 1:
            return n // 2
        elif len(c1) == 1:
            return n // 2 - c2[1][1]
        elif len(c2) == 1:
            return n // 2 - c1[1][1]
        else:
            return n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1])

if __name__ == '__main__':
    ans = main()
    print(ans)
