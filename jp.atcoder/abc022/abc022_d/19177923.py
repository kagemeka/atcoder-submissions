def read():
  import sys
  return sys.stdin.buffer.read()


def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def read_ints():
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )


def solve(n, ab):
  centroid = ab.mean(axis=1)
  import numpy as np
  dist = np.linalg.norm(
    centroid[:, None, :] - ab,
    axis=-1,
  ).sum(axis=1)
  print(dist[1] / dist[0])


def main():
  n = read_int()
  ab = read_ints().reshape(2, n, 2)
  solve(n, ab)


if __name__ == '__main__':
  main()
