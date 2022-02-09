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
  pass


def D():
  pass


if __name__ == "__main__":
  # A()
  B()
  C()
  D()
