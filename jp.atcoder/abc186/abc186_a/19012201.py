import sys


def read_ints():
  *ints, = map(
    int,
    sys.stdin.readline().split()
  )
  return ints

def solve():
  n, w = read_ints()
  print(n // w)

if __name__ == "__main__":
  solve()
