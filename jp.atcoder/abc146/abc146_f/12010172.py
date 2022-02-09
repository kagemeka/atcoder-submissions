import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r

n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()
possible = [i for i in range(n + 1) if s[i] == '0']

def main():
  trail = [0]
  cur = 0
  while True:
    if cur == n:
      break
    nxt = possible[bi_r(possible, cur + m) - 1]
    if nxt == cur:
      print(-1)
      return
    trail.append(nxt)
    cur = nxt

  res = [trail[i+1] - trail[i] for i in range(len(trail) - 1)]
  print(*res, sep=' ')

if __name__ == '__main__':
  main()
