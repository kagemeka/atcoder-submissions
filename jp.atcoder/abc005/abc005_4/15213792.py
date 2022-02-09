import sys
import numpy as np

def A():
  x, y = map(int, sys.stdin.readline().split())
  print(y//x)


def B():
  n, *t = map(int, sys.stdin.read().split())
  print(min(t))


def C():
  t = int(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline().rstrip())
  a = [int(x) for x in sys.stdin.readline().split()]
  m = int(sys.stdin.readline().rstrip())
  b = [int(x) for x in sys.stdin.readline().split()]

  i = 0
  for p in b:
    if i == n:
      print('no')
      return
    while p-a[i] > t:
      i += 1
      if i == n:
        print('no')
        return
    if a[i] > p:
      print('no')
      return
    i += 1
  print('yes')


def D():
  n = int(sys.stdin.readline().rstrip())
  d = np.array([sys.stdin.readline().split() for _ in range(n)], np.int64)
  s = d.cumsum(axis=0).cumsum(axis=1)
  s = np.pad(s, 1)
  max_del = np.zeros((n+1, n+1), dtype=np.int64)
  for y in range(1, n+1):
    for x in range(1, n+1):
      max_del[y][x] = np.amax(
        s[y:n+1, x:n+1] - s[0:n-y+1, x:n+1] - s[y:n+1, 0:n-x+1] + s[0:n-y+1, 0:n-x+1]
      )

  res = np.arange(n**2+1)[:, None]
  i = np.arange(1, n+1)
  res = max_del[i, np.minimum(res//i, n)].max(axis=1)
  q = int(sys.stdin.readline().rstrip())
  p = np.array(sys.stdin.read().split(), dtype=np.int64)
  print(*res[p], sep='\n')


if __name__ == "__main__":
  # A()
  # B()
  # C()
  D()
