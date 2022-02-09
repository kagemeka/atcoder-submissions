def readline():
  import sys
  return \
    sys.stdin.buffer.readline()


def read():
  import sys
  return sys.stdin.buffer.read()


def readline_ints():
  import numpy as np
  return np.fromstring(
    readline().decode(),
    dtype=np.int64,
    sep=' ',
  )


def read_ints():
  import numpy as np
  return np.fromstring(
    read().decode(),
    dtype=np.int64,
    sep=' ',
  )


import numpy as np
def solve(a: np.ndarray) -> None:
  print(a.sum() - a.min()*a.size)


def main():
  _, _ = readline_ints()
  a = read_ints()
  solve(a)


if __name__ == '__main__':
  main()
