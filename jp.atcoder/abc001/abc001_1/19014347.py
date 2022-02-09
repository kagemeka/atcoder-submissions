def read():
  import sys
  return sys.stdin.buffer.read()


def read_ints():
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )

def solve(h1, h2):
  print(h1 - h2)


def main():
  h1, h2 = read_ints()
  solve(h1, h2)


if __name__ == '__main__':
  main()
