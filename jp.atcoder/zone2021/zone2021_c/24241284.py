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
  combinations,
)



class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()


  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    n = read.int()
    self.__a = np.array(
      sys.stdin.read().split(),
      dtype=np.uint32,
    ).reshape(n, -1)
    self.__n = n


  def _solve(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    b = np.sort(a, axis=0)
    n = self.__n
    combs = np.array((
      *combinations(
        range(n),
        2,
      ),
    ))
    mx = a[combs].max(axis=1)
    j = np.argsort(mx, axis=1)
    res = np.minimum(
      mx[
        np.arange(j.shape[0]),
        j[:, 1],
      ],
      b[-1, j[:, 0]],
    ).max()
    print(res)


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
