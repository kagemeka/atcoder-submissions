import sys
from collections import Counter

n, t, *a = map(int, sys.stdin.read().split())

def main():
  cand = []
  mi = a[0]
  for x in a[1:]:
    cand.append(x - mi)
    mi = min(mi, x)
  c = Counter(cand)
  ans = c[max(c.keys())]
  print(ans)

if __name__ == '__main__':
  main()
