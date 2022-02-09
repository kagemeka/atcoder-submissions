import sys
from itertools import permutations, combinations

n, c = map(int, sys.stdin.readline().split())
d = [[int(x) for x in sys.stdin.readline().split()] for _ in range(c)]
grid = [[int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(n)]

cost = [[0] * c for _ in range(3)]
for i in range(n):
  for j in range(n):
    k = (i + j) % 3
    for l in range(c):
      cost[k][l] += d[grid[i][j]][l]

def main():
  res = []
  for comb in combinations(range(c), 3):
    for i, j, k in permutations(comb):
      res.append(cost[0][i] + cost[1][j] + cost[2][k])
  print(min(res))

if __name__ == '__main__':
  main()
