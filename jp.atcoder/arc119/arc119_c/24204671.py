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
from collections import (
  Counter,
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
    a = np.array(
      sys.stdin.readline()
      .split(),
      dtype=np.int64,
    )
    self.__n = n
    self.__a = a


  def _solve(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    a[::2] *= -1
    np.cumsum(a, out=a)
    c = Counter(a)
    s = c[0]
    a = np.array([*c.values()])
    s += (
      a * (a - 1) // 2
    ).sum()
    print(s)



def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
