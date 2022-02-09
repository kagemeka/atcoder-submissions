import typing



class ReadStdin:
  def __call__(
    self,
  ) -> bytes:
    return next(self.__chunks)


  def __init__(
    self,
  ) -> typing.NoReturn:
    import sys
    self.__buf = (
      sys.stdin.buffer
    )
    self.__chunks = (
      self.__read_chunks()
    )


  def int(
    self,
  ) -> int:
    return int(self())


  def __read_chunks(
    self,
  ) -> typing.Iterator[bytes]:
    while 1:
      l = self.__buf.readline()
      for chunk in l.split():
        yield chunk


  def str(
    self,
  ) -> str:
    b = self()
    return b.decode()



from abc import (
  ABC,
  abstractmethod,
)
import typing



class Solver(
  ABC,
):
  def __call__(
    self,
  ) -> typing.NoReturn:
    self._prepare()
    self._solve()


  def __init__(
    self,
  ) -> typing.NoReturn:
    ...


  @abstractmethod
  def _prepare(
    self,
  ) -> typing.NoReturn:
    ...


  @abstractmethod
  def _solve(
    self,
  ) -> typing.NoReturn:
    ...



import typing
import numpy as np
import sys
from itertools import (
  product,
)


class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__m = 5
    self.__k = 3


  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    n = read.int()
    a = np.array(
      sys.stdin.read().split(),
      dtype=np.int64,
    ).reshape(n, -1)
    self.__n = n
    self.__a = a


  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__preprocess()
    self.__binary_search()
    print(self.__res)


  def __possible(
    self,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    a = (a >= x).astype(int)
    i = self.__i
    a = (a * i).sum(axis=-1)
    return np.isin(
      self.__combs,
      np.unique(a),
    ).all(axis=1).any()


  def __binary_search(
    self,
  ) -> typing.NoReturn:
    lo, hi = 1, 1 << 40
    while hi - lo > 1:
      x = (lo + hi) // 2
      if self.__possible(x):
        lo = x
      else:
        hi = x
    self.__res = lo


  def __make_combs(
    self,
  ) -> typing.NoReturn:
    m = self.__m
    p = product(
      range(1 << m),
      repeat=3,
    )
    a = np.array([*p])
    ok = np.bitwise_or.reduce(
      a,
      axis=-1,
    ) == (1 << m) - 1
    self.__combs = a[ok]


  def __preprocess(
    self,
  ) -> typing.NoReturn:
    m = self.__m
    i = 1 << np.arange(m)
    self.__i = i
    self.__make_combs()


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
