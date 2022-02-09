import typing
import itertools


class RepeatedPermutations():
  def __call__(
    self,
    a: typing.Iterable[typing.Any],
    repeat: int,
  ) -> typing.Iterator[typing.Tuple[typing.Any]]:
    self.__a = tuple(a)
    self.__repeat = repeat
    return self.__dfs([-1] * repeat, 0)


  def __dfs(
    self,
    p: typing.List[int],
    i: int,
  ) -> typing.Iterator[typing.Tuple[typing.Any]]:
    a = self.__a
    if i == self.__repeat:
      yield tuple(a[j] for j in p)
      return
    n = len(a)
    for j in range(n):
      p[i] = j
      for _p in self.__dfs(p, i + 1):
        yield _p




def solve(s: str) -> typing.NoReturn:
  n = 10
  cand = []
  must = 0
  for i in range(n):
    if s[i] == 'o':
      cand.append(i)
      must |= 1 << i
    if s[i] == '?':
      cand.append(i)


  cnt = 0
  for prod in RepeatedPermutations()(cand, 4):
    res = 0
    for i in prod:
      res |= 1 << i
    cnt += must & ~res == 0

  print(cnt)



def main() -> typing.NoReturn:
  s = input()
  solve(s)


main()
