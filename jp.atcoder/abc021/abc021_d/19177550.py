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

class ChooseMod(Modular):
  def __init__(
      self,
      n: int=1<<20,
      **kwargs):
    super(ChooseMod, self).__init__(
      **kwargs,
    )
    self.fact = self.factorial(n)
    self.inv_fact = \
      self.inverse_factorial(n)


  def __call__(self, n, r):
    return self._choose(n, r)


  def _choose(self, n: int, r: int):
    bl = (0<=r) & (r<=n)
    p = self.mod
    return bl * self.fact[n] \
      * self.inv_fact[r] % p \
      * self.inv_fact[n-r] % p


def solve(n, k):
  c = ChooseMod(n+k, mod=10**9+7)
  print(c(n+k-1, k))


def main():
  n, k = read_ints()
  solve(n, k)


if __name__ == '__main__':
  main()
