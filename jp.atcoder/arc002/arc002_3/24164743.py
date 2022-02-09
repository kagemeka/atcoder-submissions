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
import itertools


class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__pool = 'ABXY'


  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    self.__n = read.int()
    self.__s = read.str()


  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__make_combs()
    cnt = 1 << 10
    for comb in self.__combs:
      self.__comb = set(comb)
      c = self.__calc()
      cnt = min(cnt, c)
    print(cnt)


  def __calc(
    self,
  ) -> int:
    n = self.__n
    s = self.__s + '$'
    comb = self.__comb
    inf = 1 << 10
    dp = [
      [inf] * 2
      for _ in range(n + 1)
    ]
    dp[0][0] = 0
    for i in range(n):
      dp[i + 1][0] = min(
        dp[i][0] + 1,
        dp[i][1],
      )
      w = s[i:i + 2]
      if not w in comb:
        continue
      dp[i + 1][1] = (
        dp[i][0] + 1
      )
    return dp[-1][0]


  def __make_combs(
    self,
  ) -> typing.NoReturn:
    p = itertools.product(
      self.__pool,
      repeat=2,
    )
    p = map(
      lambda x: ''.join(x),
      p,
    )
    c = itertools.combinations(
      p,
      2,
    )
    self.__combs = c




def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
