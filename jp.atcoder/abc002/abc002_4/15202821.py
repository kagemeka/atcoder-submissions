import sys

def A():
  x, y = map(int, sys.stdin.readline().split())
  print(max(x, y))


def B():
  vowels = set('aeiou')
  s = sys.stdin.readline().rstrip()
  t = ''
  for c in s:
    if c in vowels: continue
    t += c
  print(t)


def C():
  *coords, = map(int, sys.stdin.readline().split())
  def triangle_area(x0, y0, x1, y1, x2, y2):
    x1 -= x0; x2 -= x0; y1 -= y0; y2 -= y0;
    return abs(x1*y2 - x2*y1) / 2
  print(triangle_area(*coords))


def D():
  n, m = map(int, sys.stdin.readline().split())
  aquaintance = [set() for _ in range(n)]
  for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1; y -= 1
    aquaintance[x].add(y)
    aquaintance[y].add(x)

  cand = []
  for i in range(1, 1<<n):
    comb = [j for j in range(n) if i>>j & 1]
    if len(set(comb)&aquaintance[comb[0]]) == len(comb)-1:
      cand.append(len(comb))

  print(max(cand))
  pass


if __name__ == "__main__":
  # A()
  # B()
  # C()
  D()
