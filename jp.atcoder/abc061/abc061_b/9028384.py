import sys
from collections import Counter

n, m, *r = map(int, sys.stdin.read().split())

def main():
    c = Counter(r)
    for v in range(1, n+1):
        yield c.get(v, 0)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
