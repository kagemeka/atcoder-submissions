import sys

def A():
  print(int(sys.stdin.readline().rstrip())*2)
  pass


def B():
  c = [sys.stdin.readline().rstrip() for _ in range(4)]
  for l in c[::-1]:
    print(l[::-1])

def C():
  pass


def D():
  pass

if __name__ == "__main__":
  # A()
  B()
  C()
  D()
