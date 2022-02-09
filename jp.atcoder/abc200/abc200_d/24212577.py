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
import dataclasses


@dataclasses.dataclass
class Message():
  ok: str
  ng: str



class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__k = 200
    self.__msg = Message(
      ok='yes',
      ng='no',
    )


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
    self.__calc_dp()
    msg = self.__msg
    if self.__dp is None:
      print(msg.ng)
      return
    b = self.__recover(
      self.__to_0,
    )
    c = self.__recover(
      self.__to_1,
    )
    print(msg.ok)
    print(len(b), *b)
    print(len(c), *c)


  def __recover(
    self,
    to: typing.Tuple[int, int],
  ) -> typing.List[int]:
    i, j = to
    dp = self.__dp
    a = self.__a
    k = self.__k
    res = []
    while i > 0:
      i -= 1
      if (
        dp[i, j]
        == dp[i + 1, j]
      ): continue
      res.append(i + 1)
      j = (j - a[i]) % k
    return res[::-1]


  def __calc_dp(
    self,
  ) -> typing.NoReturn:
    n = self.__n
    k = self.__k
    dp = np.zeros(
      (n + 1, k),
      dtype=np.int8,
    )
    dp[0, 0] = 1
    a = self.__a
    a %= k
    j = np.arange(k)
    for i in range(n):
      nx = dp[i].copy()
      l = (j + a[i]) % k
      nx[l] += dp[i, j]
      dp[i + 1] = nx
      ls = np.argwhere(nx == 2)
      if ls.size == 0: continue
      j = ls.ravel()[-1]
      i += 1
      to_0 = (i, j)
      if j != 0:
        to_1 = (i - 1, j)
        break
      if i == n: continue
      j = (j + a[i]) % k
      to_1 = (i + 1, j)
      break
    else:
      self.__dp = None
      return
    self.__dp = dp
    self.__to_0 = to_0
    self.__to_1 = to_1



def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
