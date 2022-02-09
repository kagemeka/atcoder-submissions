import sys
from bisect import bisect_left as bi_l

n, t, *a = map(int, sys.stdin.read().split())

def main():
  cand = []
  mi = a[0]
  for x in a[1:]:
    cand.append(x - mi)
    mi = min(mi, x)
  cand.sort()
  ans = n - bi_l(cand, cand[-1]) - 1
  print(ans)

if __name__ == '__main__':
  main()
