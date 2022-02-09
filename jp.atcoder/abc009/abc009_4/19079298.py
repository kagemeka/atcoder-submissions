def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def readline_ints():
  import numpy as np
  return np.fromstring(
    string=readline().decode(),
    dtype=np.int64,
    sep=' ',
  )


def bitwise_dot(a, b):
  import numpy as np
  return np.bitwise_xor.reduce(
    a[:, None, :] & b.T[None, ...],
    axis=-1,
  )


def bitwise_matrix_pow(a, n):
  import numpy as np
  if n==0:
    mask = (1<<32) - 1
    return np.eye(
      len(a),
      dtype=np.uint32,
    ) * mask
  res = bitwise_matrix_pow(a, n//2)
  res = bitwise_dot(res, res)
  if n&1: res = bitwise_dot(res, a)
  return res


def solve(k, m, a, c):
  import numpy as np
  mask = (1<<32) - 1
  d = np.eye(
    N=k, M=k, k=-1,
    dtype=np.uint32,
  ) * mask
  d[0] = c
  if m <= k:
    print(a[m-1])
    return

  res = bitwise_dot(
    bitwise_matrix_pow(d, m-k),
    a[::-1][:, None],
  )
  print(res.ravel()[0])


def main():
  k, m = readline_ints()
  a = readline_ints()
  c = readline_ints()
  solve(k, m, a, c)


if __name__ == '__main__':
  main()
