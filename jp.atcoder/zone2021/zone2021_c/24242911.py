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
import sys
import numpy as np
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
    self.__a = np.array(
      sys.stdin.read().split(),
      dtype=np.int64,
    ).reshape(n, -1)
    self.__n = n


  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__make_combs()
    m = self.__m
    i = np.arange(
      1 << m,
    )[:, None] >> np.arange(
      m,
    ) & 1
    i[i == 0] = 1 << 30
    a = np.sort(
      np.amin(
        self.__a[:, None] * i,
        axis=-1,
      ),
      axis=0,
    )[-1]
    a[0] = 0
    res = a[self.__combs].min(
      axis=1,
    ).max()
    print(res)


  def __make_combs(
    self,
  ) -> typing.NoReturn:
    m = self.__m
    combs = np.array((*product(
      range(1 << m),
      repeat=self.__k,
    ),))
    ok = np.bitwise_or.reduce(
      combs,
      axis=-1,
    ) == (1 << m) - 1
    self.__combs = combs[ok]



def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
