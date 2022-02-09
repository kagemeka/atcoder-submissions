def read():
  import sys
  return sys.stdin.buffer.read()


def read_ints():
  *ints, = map(
    int,
    read().split(),
  )
  return ints


class Algebra:
  ...


class Modular(Algebra):
  def __init__(
      self,
      mod=10**9+7,
      **kwargs):
    super(Modular, self).__init__(
      **kwargs,
    )
    self.mod = mod


  def inverse(self, n: int):
    p = self.mod
    return self.pow(n, p-2)


  def cumprod(self, a):
    import numpy as np
    l = len(a)
    n = int(np.sqrt(l) + 1)
    a = np.resize(a, (n, n))

    for i in range(n-1):
      a[:, i+1] *= a[:, i]
      a[:, i+1] %= self.mod

    for i in range(n-1):
      a[i+1] *= a[i, -1]
      a[i+1] %= self.mod

    return np.ravel(a)[:l]


  def factorial(self, n: int):
    import numpy as np
    fact = np.arange(n+1)
    fact[0] = 1
    return self.cumprod(fact)


  def inverse_factorial(
      self, n: int):
    import numpy as np
    fact = self.factorial(n)

    inv_fact = np.arange(1, n+2)
    inv_fact[-1] = self.inverse(
      fact[-1],
    )

    inv_fact = self.cumprod(
      inv_fact[::-1],
    )[n::-1]

    return inv_fact


  def pow(self, x, n):
    if n == 0: return 1
    x %= self.mod
    y = self.pow(x, n>>1)
    y = y * y % self.mod
    if n&1: y = y * x % self.mod
    return y


  def matrix_pow(self, a, n):
    import numpy as np
    assert a.ndim == 2 and \
      a.shape[0] == a.shape[1]
    if n == 0:
      m = a.shape[0]
      e = np.identity(m, np.int64)
      return e
    a %= self.mod
    b = self.matrix_pow(a, n>>1)
    b = np.dot(b, b) % self.mod
    if n&1:
      b = np.dot(b, a) % self.mod
    return b


def solve(a, b, c):
  p = 10 ** 9  + 7
  m = Modular(mod=p)
  denom = m.inverse(a*b - b*c + c*a)
  w = (b*c - a*b) % p * denom % p
  h = (b*c - a*c) % p * denom % p
  print(h, w)


def main():
  a, b, c = read_ints()
  solve(a, b, c)


if __name__ == '__main__':
  main()
