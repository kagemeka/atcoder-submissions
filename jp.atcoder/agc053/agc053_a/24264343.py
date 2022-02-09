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


class CompressArray():
  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]

  def __call__(
    self,
    a: np.array,
  ) -> np.array:
    v = np.unique(a)
    self.__v = v
    i = np.searchsorted(v, a)
    return i



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
    self.__n = read.int()
    self.__s = read()
    self.__a = np.array(
      sys.stdin.readline()
      .split(),
      dtype=np.int16,
    )


  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__preprocess()
    s = self.__s
    a = self.__a
    ls = []
    while 1:
      a -= s
      if self.__is_ok():
        ls.append(s)
        continue
      ls.append(a + s)
      break
    print(len(ls))
    for a in ls:
      print(*a)


  def __is_ok(
    self,
  ) -> bool:
    a = self.__a
    if (a[:-1] == a[1:]).any():
      return False
    a = a[:-1] < a[1:]
    a = a * 2 - 1
    a = np.pad(a, (1, 0))
    np.cumsum(a, out=a)
    a = self.__compress(a)
    s = self.__s
    return (a == s).all()


  def __preprocess(
    self,
  ) -> typing.NoReturn:
    s = self.__s
    s = np.array(
      list(s),
      dtype=np.int64,
    ) == ord('<')
    s = s * 2 - 1
    s = np.pad(s, (1, 0))
    np.cumsum(s, out=s)
    s = self.__compress(s)
    self.__s = s


  def __compress(
    self,
    a: np.array,
  ) -> np.array:
    return CompressArray()(a)



def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
