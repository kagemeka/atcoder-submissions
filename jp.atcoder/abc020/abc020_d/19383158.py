class Reader:

  @staticmethod
  def readline():
    import sys
    return sys.stdin.buffer \
      .readline().rstrip()


  @classmethod
  def read_int(cls):
    i = int(cls.readline())
    return i


  @classmethod
  def read_str(cls):
    s = cls.readline().decode()
    return s


  @classmethod
  def readline_ints(cls):
    *ints, = map(
      int,
      cls.readline().split(),
    )
    return ints


  @classmethod
  def readline_strs(cls):
    s = cls.read_str().split()
    return s


  @staticmethod
  def read():
    import sys
    i = sys.stdin.buffer.read()
    return i


  @classmethod
  def read_ints(cls):
    *ints, = map(
      int,
      cls.read().split(),
    )
    return ints


  @classmethod
  def read_strs(cls):
    return cls.read() \
      .decode().split()


  @staticmethod
  def readlines():
    import sys
    lines = sys.stdin.buffer \
      .readlines()
    lines = [
      l.rstrip()
      for l in lines
    ]
    return lines


class ReaderNumpy(Reader):

  @classmethod
  def readline_ints(cls):
    import numpy as np
    return np.fromstring(
      string=cls.read_str(),
      dtype=np.int64,
      sep=' ',
    )


  @classmethod
  def read_ints(cls):
    import numpy as np
    return np.fromstring(
      string=cls.read() \
        .decode(),
      dtype=np.int64,
      sep=' ',
    )


MOD = 10 ** 9 + 7

class Modular:

  def __init__(
      self,
      n: int,
      mod: int=MOD):
    self.value = n
    self.value %= mod
    self.mod = mod


  def __repr__(self) -> str:
    return f'{self.value}'


  def clone(self):
    return self.__class__(
      self.value,
    )

  @classmethod
  def modularize(cls, other):
    if type(other) == int:
      other = cls(other)
    return other


  def __iadd__(self, other):
    other = self.modularize(
      other,
    )
    self.value += other.value
    self.value %= self.mod
    return self


  def __add__(self, other):
    res = self.clone()
    res += other
    return res


  def __radd__(self, other):
    return self.clone() + other


  def __neg__(self):
    return self.__class__(
      -self.value,
    )


  def __sub__(self, other):
    res = self.clone()
    res += -other
    return res


  def __rsub__(self, other):
    other = self.modularize(
      other,
    )
    return other - self


  def __imul__(self, other):
    other = self.modularize(
      other,
    )
    self.value *= other.value
    self.value %= self.mod
    return self


  def __mul__(self, other):
    res = self.clone()
    res *= other
    return res


  def __rmul__(self, other):
    return self.clone() * other


  def __truediv__(self, other):
    other = self.modularize(
      other,
    )
    res = self.clone()
    res *= other.invert()
    return res


  def __rtruediv__(
      self, other):
    other = self.modularize(
      other,
    )
    return other / self


  def __floordiv__(
      self, other):
    return self / other


  def __rfloordiv__(
      self, other):
    return other / self


  def pow(self, n):
    if n == 0:
      return self.__class__(1)
    a = self.pow(n>>1)
    a *= a
    if n&1: a *= self
    return a


  def __ipow__(self, other):
    other = self.modularize(
      other,
    )

    self.value = pow(
      self.value,
      other.value,
      self.mod,
    )
    return self


  def __pow__(self, other):
    res = self.clone()
    res **= other
    return res


  def __rpow__(self, other):
    other = self.modularize(
      other,
    )
    return other ** self


  def invert(self):
    return \
      self ** (self.mod - 2)

Mint = Modular


def find_divisors(n: int=...):
  m = int(n**.5) + 1
  divisors = []
  for x in range(1, m):
    if n%x: continue
    divisors.append(x)
    if n//x != x:
      divisors.append(n//x)
  divisors.sort()
  return divisors


class Solver:

  def __init__(self):
    self.reader = Reader()
    # self.reader = ReaderNumpy()


  def __prepare(self):
    reader = self.reader
    n, k = reader \
      .readline_ints()
    self.n, self.k = n, k


  def __solve(self):
    n, k = self.n, self.k
    divs = find_divisors(k)
    divs = divs[::-1]
    l = len(divs)

    s = [
      Mint(0)
      for _ in range(l)
    ]

    for i in range(l):
      d = divs[i]
      q = Mint(n // d)
      s[i] = (1+q) * q / 2 * d
      for j in range(i):
        if divs[j] % d != 0:
          continue
        s[i] -= s[j]

    res = 0
    for i in range(l):
      res += s[i] / divs[i]

    res *= k
    print(res)

    ...


  def run(self):
    self.__prepare()
    self.__solve()


def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    solver = Solver()
    solver.run()


if __name__ == '__main__':
  main()
