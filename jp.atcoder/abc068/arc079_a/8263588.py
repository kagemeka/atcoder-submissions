import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
ab = [tuple(int(x) for x in input().split()) for _ in range(m)]

for i in range(2, n):
    if (1, i) in ab and (i, n) in ab: print('POSSIBLE'); exit()
print('IMPOSSIBLE')
