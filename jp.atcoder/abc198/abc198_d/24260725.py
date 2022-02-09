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
from itertools import (
  permutations,
)
import numpy as np




class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__m = 10


  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    self.__s1 = read()
    self.__s2 = read()
    self.__s3 = read()


  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__preprocess()
    s1 = self.__s1
    s2 = self.__s2
    s3 = self.__s3
    a = np.unique(
      np.hstack((s1, s2, s3)),
    )
    m = self.__m
    if a.size > m:
      print('UNSOLVABLE')
      return
    s1 = np.searchsorted(a, s1)
    s2 = np.searchsorted(a, s2)
    s3 = np.searchsorted(a, s3)
    n = len(a)
    p = permutations(
      range(m),
      n,
    )
    p = np.array((*p,))
    (s1, s2, s3) = (
      p[:, s]
      * 10 ** np.arange(
        len(s),
      )[::-1]
      for s in (s1, s2, s3)
    )
    (ok1, ok2, ok3) = (
      s[:, 0] != 0
      for s in (s1, s2, s3)
    )
    ok = ok1 & ok2 & ok3
    (s1, s2, s3) = (
      s[ok].sum(axis=1)
      for s in (s1, s2, s3)
    )
    i = np.argwhere(
      s1 + s2 == s3,
    ).ravel()
    if i.size == 0:
      print('UNSOLVABLE')
      return
    i = i[0]
    print(
      s1[i],
      s2[i],
      s3[i],
      sep='\n',
    )


  def __preprocess(
    self,
  ) -> typing.NoReturn:
    (
      self.__s1,
      self.__s2,
      self.__s3,
    ) = (
      np.array(
        list(s),
        dtype=np.int64,
      ) - ord('a')
      for s in (
        self.__s1,
        self.__s2,
        self.__s3,
      )
    )

def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
