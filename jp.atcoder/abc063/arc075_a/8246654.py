import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input().rstrip())
score = [int(input().rstrip()) for _ in range(N)]
score.sort(reverse=1)

for s in score:
    if s % 10 != 0:
        break
else:
    print(0)


for i in range(N, 0, -1):
    for c in combinations(score, i):
        if sum(c) % 10 == 0:
            continue
        else:
            print(sum(c))
            exit()
