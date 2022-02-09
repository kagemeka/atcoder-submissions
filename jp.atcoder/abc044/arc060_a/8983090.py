import sys
from collections import defaultdict

n, a, *x = map(int, sys.stdin.read().split())

def main():
    for i in range(n):
        x[i] -= a

    c = defaultdict(int)
    c[0] = 1
    for i in x:
        for val, cnt in tuple(c.items()):
            c[val+i] += cnt
    ans = c[0] - 1
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
