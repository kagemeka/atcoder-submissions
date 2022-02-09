import sys

def A():
  n = int(sys.stdin.readline().rstrip())
  charge = (n+999)//1000 * 1000 - n
  print(charge)


from collections import Counter
def B():
  n, *s = sys.stdin.read().split()
  c = Counter(s)
  for v in 'AC, WA, TLE, RE'.split(', '):
    print(f'{v} x {c[v]}')


def C():
  h, w, k = map(int, sys.stdin.readline().split())
  c = [sys.stdin.readline().rstrip() for _ in range(h)]
  tot = 0
  for i in range(1<<h):
    for j in range(1<<w):
      cnt = 0
      for y in range(h):
        for x in range(w):
          if i>>y & 1 or j>>x & 1:
            continue
          cnt += c[y][x] ==  '#'
      tot += cnt == k
  print(tot)


def D():
  n, *a = map(int, sys.stdin.read().split())
  a.sort(reverse=True)
  res = a[0] + sum(a[1:1+(n-2)//2])*2 + a[1+(n-2)//2]*(n & 1)
  print(res)


def E():
  pass


def F():
  pass

if __name__ == "__main__":
  # A()
  # B()
  # C()
  D()
  E()
  F()
