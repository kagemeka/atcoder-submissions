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
  chain,
)
from bisect import (
  bisect_left,
)



class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__n = 3
    self.__m = 10

  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    n = self.__n
    self.__s = [
      read()
      for _ in range(n)
    ]


  def _solve(
    self,
  ) -> typing.NoReturn:
    ok = self.__preprocess()
    if not ok: return
    for p in self.__perms:
      self.__p = p
      ok = self.__check()
      if ok: return
    print('UNSOLVABLE')



  def __check(
    self,
  ) -> bool:
    s = self.__s
    p = self.__p
    s = [
      [p[i] for i in x]
      for x in s
    ]
    if any(
      x[0] == 0 for x in s
    ): return False
    d = self.__d
    for i in range(self.__n):
      l = len(s[i])
      s[i] = sum(
        d[i][j] * s[i][j]
        for j in range(l)
      )
    ok = s[0] + s[1] == s[2]
    if ok:
      print(*s, sep='\n')
    return ok


  def __preprocess(
    self,
  ) -> bool:
    s = self.__s
    s = [list(x) for x in s]
    a = chain.from_iterable(s)
    a = sorted(set(a))
    s = [
      [
        bisect_left(a, c)
        for c in x
      ] for x in s
    ]
    r = len(a)
    if r > self.__m:
      print('UNSOLVABLE')
      return False
    perms = permutations(
      range(self.__m),
      r,
    )
    self.__s = s
    self.__perms = perms
    self.__d = [
      [
        pow(10, i)
        for i in range(len(x))
      ][::-1] for x in s
    ]
    return True


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
