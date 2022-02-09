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
  pass


if __name__ == "__main__":
  # A()
  # B()
  C()
  D()
