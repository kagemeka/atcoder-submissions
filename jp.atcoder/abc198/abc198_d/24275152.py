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
  chain,
)
from bisect import (
  bisect_left,
)


class VerbalArithmetic():
  def __call__(
    self,
    words: typing.List[str],
    result: typing.List[str],
    zero_ok: bool = True,
  ) -> typing.List[
    typing.Dict[str, int],
  ]:
    s = words
    s.append(result)
    self.__s = s
    self.__zero_ok = zero_ok
    self.__preprocess()
    self.__search()
    return self.__res


  def __preprocess(
    self,
  ) -> bool:
    s = self.__s
    n = len(s)
    m = max(map(len, s))
    self.__n, self.__m = n, m
    s = [list(x) for x in s]
    a = chain.from_iterable(s)
    a = sorted(set(a))
    s = [
      [
        bisect_left(a, c)
        for c in x
      ] for x in s
    ]
    self.__a = a
    self.__s = s
    self.__l = [None] * 10
    self.__d = [None] * len(a)
    self.__res = []
    self.__i = self.__j = 0
    self.__v = 0


  def __search(
    self,
  ) -> bool:
    n, m = self.__n, self.__m
    i, j = self.__i, self.__j
    if j >= m:
      self.__check_res()
      return
    if i == n:
      self.__search_nxt_col()
      return
    self.__w = w = self.__s[i]
    if j >= len(w):
      self.__skip_row()
      return
    self.__check_sign()
    self.__c = c = w[~j]
    if self.__d[c] is None:
      self.__non_fixed_search()
      return
    self.__fixed_search()


  def __check_sign(
    self,
  ) -> typing.NoReturn:
    i, n = self.__i, self.__n
    sign = (i < n - 1) * 2 - 1
    self.__sign = sign


  def __check_zero(
    self,
  ) -> bool:
    j = self.__j
    return (
      self.__x
      or j != len(self.__w) - 1
      or self.__zero_ok
      and j == 0
    )


  def __fixed_search(
    self,
  ) -> typing.NoReturn:
    x = self.__d[self.__c]
    self.__x = x
    if not self.__check_zero():
      return
    i, v = self.__i, self.__v
    sign = self.__sign
    self.__i += 1
    self.__v += sign * x
    self.__search()
    self.__i, self.__v = i, v


  def __non_fixed_search(
    self,
  ) -> typing.NoReturn:
    l = self.__l
    i, j = self.__i, self.__j
    w = self.__w
    v = self.__v
    sign = self.__sign
    l, d = self.__l, self.__d
    c = self.__c
    for x in range(10):
      if l[x] is not None:
        continue
      self.__x, self.__w = x, w
      self.__j = j
      ok = self.__check_zero()
      if not ok: continue
      d[c], l[x] = x, c
      self.__i += 1
      self.__v += sign * x
      self.__search()
      d[c] = l[x] = None
      self.__i, self.__v = i, v


  def __check_res(
    self,
  ) -> typing.NoReturn:
    if self.__v != 0: return
    d, a = self.__d, self.__a
    res = self.__res
    res.append(dict(zip(a, d)))


  def __skip_row(
    self,
  ) -> typing.NoReturn:
    i = self.__i
    self.__i += 1
    self.__search()
    self.__i = i


  def __search_nxt_col(
    self,
  ) -> typing.NoReturn:
    v = self.__v
    i, j = self.__i, self.__j
    if v % 10 != 0: return
    self.__j += 1
    self.__i = 0
    self.__v //= 10
    self.__search()
    self.__i, self.__j = i, j
    self.__v = v



class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__n = 3


  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    n = self.__n
    self.__s = [
      read() for _ in range(n)
    ]


  def _solve(
    self,
  ) -> typing.NoReturn:
    s = self.__s
    fn = VerbalArithmetic()
    res = fn(
      s[:-1],
      s[-1],
      zero_ok=False,
    )
    if not res:
      print('UNSOLVABLE')
      return
    d = res[0]
    for w in s:
      w = [d[c] for c in w]
      w = ''.join(map(str, w))
      print(w)


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
