import sys

def A():
  x, y = map(int, sys.stdin.readline().split())
  print(y//x)


def B():
  n, *t = map(int, sys.stdin.read().split())
  print(min(t))


def C():
  pass


def D():
  pass



if __name__ == "__main__":
  # A()
  B()
  C()
  D()
