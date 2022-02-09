import typing
import sys
import bisect



class UnionFind():
  def __init__(
    self,
    n: int,
    length: typing.List[int],
  ) -> typing.NoReturn:
    self.__a = [-1] * n
    self.__l = length
    assert len(length) == n


  def find(
    self,
    u: int,
  ) -> int:
    a = self.__a
    if a[u] < 0: return u
    a[u] = self.find(a[u])
    return a[u]


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return
    a = self.__a
    l = self.__l
    if a[u] > a[v]: u, v = v, u
    a[u] += a[v]
    l[u] += l[v]
    a[v] = u


  def length(
    self,
    u: int,
  ) -> int:
    return self.__l[self.find(u)]


def main() -> typing.NoReturn:
  l, q = map(int, input().split())
  cx = map(int, sys.stdin.read().split())
  cx = zip(*[cx] * 2)
  cx = list(cx)

  a = [l]
  for c, x in cx:
    if c == 2: continue
    a.append(x)
  a.sort()
  n = len(a)
  length = a.copy()
  for i in range(n - 1):
    length[i + 1] = a[i + 1] - a[i]
  uf = UnionFind(n, length)
  res = []
  for c, x in cx[::-1]:
    i = bisect.bisect_left(a, x)
    if c == 1:
      uf.unite(i, i + 1)
      continue
    res.append(uf.length(i))

  print(*res[::-1], sep='\n')










main()
