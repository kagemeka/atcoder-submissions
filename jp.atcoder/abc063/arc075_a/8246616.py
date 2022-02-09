import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input().rstrip())
s = [int(input().rstrip()) for _ in range(N)]
s.sort(reverse=1)

for s in s:
    if s % 10 != 0:
        break
else:
    print(0)

for i in range(N, 0, -1):
    for c in combinations(s, i):
        if sum(c) % 10 == 0:
            continue
        else:
            print(sum(c))
            exit()
