import sys

def A():
  n = int(sys.stdin.readline().rstrip())
  charge = (n+999)//1000 * 1000 - n
  print(charge)
  pass

from collections import Counter
def B():
  n, *s = sys.stdin.read().split()
  c = Counter(s)
  for v in 'AC, WA, TLE, RE'.split(', '):
    print(f'{v} x {c[v]}')
  pass


def C():
  pass


def D():
  pass


def E():
  pass


def F():
  pass

if __name__ == "__main__":
  # A()
  B()
  C()
  D()
  E()
  F()
