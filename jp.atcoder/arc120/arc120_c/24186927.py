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



class CompressArray():
  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]


  def __call__(
    self,
    a: typing.Iterable[int],
  ) -> typing.List[int]:
    a = sorted(
      enumerate(a),
      key=lambda x: x[1],
    )
    n = len(a)
    b = [None] * n
    v = [None] * n
    i, mn = -1, -float('inf')
    for j, x in a:
      if x > mn:
        i += 1
        v[i] = x
        mn = x
      b[j] = i
    self.__v = v
    return b



import typing


class FenwickTree():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__buf = [0] * (n + 1)


  def add(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    b = self.__buf
    n = len(b)
    while i < n:
      b[i] += x
      i += i & -i


  def sum(
    self,
    i: int,
  ) -> int:
    b = self.__buf
    s = 0
    while i > 0:
      s += b[i]
      i -= i & -i
    return s



import typing


class InversionCount():
  def __call__(
    self,
    a: typing.List[int],
  ) -> int:
    self.__a = a
    self.__compress()
    self.__calc()
    return self.__cnt


  def __calc(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    n = len(a)
    ft = FenwickTree(n)
    c = 0
    for i in range(n):
      x = a[i]
      c += i - ft.sum(x)
      ft.add(x + 1, 1)
    self.__cnt = c


  def __compress(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    fn = CompressArray()
    self.__a = fn(a)




import typing
import sys
import numpy as np



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
    a, b = np.array(
      sys.stdin.read().split(),
      dtype=np.int64,
    ).reshape(2, n)
    self.__n = n
    self.__a = a
    self.__b = b



  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__preprocess()
    self.__enumerate_sort()
    if not self.__achievable():
      print(-1); return
    self.__count_inversion()
    print(self.__res)


  def __count_inversion(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    b = self.__b
    n = a.shape[0]
    c = np.zeros(n, dtype=int)
    c[a[:, 0]] = b[:, 0]
    fn = InversionCount()
    self.__res = fn(c)


  def __enumerate_sort(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    b = self.__b
    self.__a = np.array(sorted(
      enumerate(self.__a),
      key=lambda x: x[1],
    ))
    self.__b = np.array(sorted(
      enumerate(self.__b),
      key=lambda x: x[1],
    ))


  def __achievable(
    self,
  ) -> bool:
    return ((
      self.__a[:, 1]
      == self.__b[:, 1]
    ).all())



  def __preprocess(
    self,
  ) -> typing.NoReturn:
    n = self.__n
    i = np.arange(n)
    self.__a += i
    self.__b += i


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
