import sys
from functools import lru_cache
inf = float('inf')

n, A, B, C, *l = map(int, sys.stdin.read().split())

@lru_cache
def cost(a, b, c, cnt, i):
    if i == n:
        if not (a and b and c): return inf
        return abs(A - a) + abs(B - b) + abs(C - c) + 10 * (cnt - 3)
    return min(cost(a, b, c, cnt, i+1),
               cost(a+l[i], b, c, cnt+1, i+1),
               cost(a, b+l[i], c, cnt+1, i+1),
               cost(a, b, c+l[i], cnt+1, i+1))

def main():
    print(cost(0, 0, 0, 0, 0))

if __name__ ==  '__main__':
    main()
