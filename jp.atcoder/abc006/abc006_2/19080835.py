def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def matrix_mod_pow(a, n, mod):
  import numpy as np
  assert a.ndim == 2 and \
    a.shape[0] == a.shape[1]
  if n == 0:
    m = a.shape[0]
    e = np.identity(m, np.int64)
    return e
  a %= mod
  b = matrix_mod_pow(a, n//2, mod)
  b = np.dot(b, b) % mod
  if n&1: b = np.dot(b, a) % mod
  return b


def solve(n):
  import numpy as np
  a = np.array([0, 0, 1])
  if n < 3:
    print(a[n])
    return
  a = a[::-1][:, None]
  c = np.eye(
    N=3, M=3, k=-1,
    dtype=np.int64,
  )
  c[0] = 1
  global mod
  c = matrix_mod_pow(c, n-2, mod)
  a = np.dot(c, a) % mod
  print(a.ravel()[0])


def main():
  n = read_int() - 1
  global mod
  mod = 10_007
  solve(n)


if __name__ == '__main__':
  main()
