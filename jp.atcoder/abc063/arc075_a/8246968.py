import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input().rstrip())
score = [int(input().rstrip()) for _ in range(N)]
score.sort(reverse=1)

s_multiple_of_10 = [s for s in score if s % 10 == 0]
if len(s_multiple_of_10) == N: print(0)
s_not_multiple_of_10 = [s for s in score if s % 10 != 0]

# combinationsでも、先に１０の倍数を除外してから処理したらどうだろう
for i in range(len(s_not_multiple_of_10), 0, -1):
    for c in combinations(s_not_multiple_of_10, i):
        if sum(c) % 10 == 0:
            continue
        else:
            print(sum(c) + sum(s_multiple_of_10))
            exit()
