import sys

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
  pass


def D():
  pass

if __name__ == "__main__":
  # A()
  B()
  C()
  D()
