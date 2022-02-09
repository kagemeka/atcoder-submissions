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
      dtype=np.int32,
    ).reshape(n, -1)
    self.__n = n


  def _solve(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    n = self.__n
    m = self.__m
    k = self.__k
    dp = np.zeros(
      (k + 1, 1 << m),
      dtype=np.int64,
    )
    b = np.arange(1 << m)
    c = b[:, None]
    i = c >> np.arange(m) & 1
    i[i == 0] = 1 << 30
    a = np.amin(
      self.__a[:, None] * i,
      axis=-1,
    )
    mask = c - b == c ^ b
    prev = c & ~b
    dp[0, 0] = 1 << 30
    for i in range(n):
      tmp = np.minimum(
        a[i],
        dp[:-1, prev] * mask,
      ).max(axis=-1)
      np.maximum(
        dp[1:],
        tmp,
        out=dp[1:],
      )
    print(dp[-1, -1])


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
