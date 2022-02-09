import sys
import numpy as np


def A():
  s, t = map(int, sys.stdin.readline().split())
  print(t-s+1)


from collections import defaultdict
def B():
  n, *s = sys.stdin.read().split()
  res = defaultdict(int)
  for name in s:
    res[name] += 1
  print(sorted(res.items(), key=lambda x: x[1])[-1][0])


def C():
  n, *a = map(int, sys.stdin.read().split())
  a = np.array(a)
  c = np.bincount(a, minlength=101)
  for i in range(50, 0, -1):
    c[i*2:101:i] += c[i]
  a = c[a]
  ans = np.sum((a+1)//2/a)
  print(ans)

def D():
  pass

if __name__ == "__main__":
  # A()
  # B()
  C()
  D()
