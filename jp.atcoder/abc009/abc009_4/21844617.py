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



import numpy as np
def solve(k, m, a, c):
  dtype = np.uint32
  bitmat = BitwiseMatUtil(
    dtype=dtype,
  )
  d = np.eye(
    N=k,
    M=k,
    k=-1,
    dtype=dtype,
  ) * bitmat.mask

  d[0] = c
  if m <= k:
    print(a[m - 1])
    return

  a = a[::-1][:, None]
  d = bitmat.pow(d, m - k)
  a = bitmat.dot(d, a)
  print(a.ravel()[0])


def main():
  k, m = readline_ints()
  a = readline_ints()
  c = readline_ints()
  solve(k, m, a, c)



class BitwiseMatUtil:


  def __init__(
    self,
    dtype: np.dtype=np.uint32,
  ):
    self.dtype = dtype


  @property
  def mask(self):
    return np.iinfo(
      self.dtype,
    ).max


  @property
  def mul_identity(
    self,
  ):
    e = np.identity(
      self.n,
      dtype=self.dtype,
    )
    np.fill_diagonal(
      e,
      self.mask,
    )
    return e


  @staticmethod
  def dot(
    a: np.ndarray,
    b: np.ndarray,
  ) -> np.ndarray:
    c = np.bitwise_xor.reduce(
      a[:, None, :]
      & b.T[None, ...],
      axis=-1,
    )
    return c


  def pow(
    self,
    a: np.ndarray,
    n: int,
  ) -> np.ndarray:
    if n == 0:
      self.n = a.shape[0]
      return self.mul_identity
    x = self.pow(a, n >> 1)
    x = self.dot(x, x)
    if n & 1:
      x = self.dot(x, a)
    return x


if __name__ == '__main__':
  main()
