import typing
import sys


class UnionFind():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__p = list(range(n))
    self.__s = [1] * n


  def find(
    self,
    u: int,
  ) -> int:
    p = self.__p
    if p[u] == u: return u
    p[u] = self.find(p[u])
    return p[u]


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return
    p, s = self.__p, self.__s
    if s[u] < s[v]: u, v = v, u
    s[u] += s[v]
    p[v] = u


  def size(
    self,
    u: int,
  ) -> int:
    return self.__s[self.find(u)]



def main() -> typing.NoReturn:
  n = int(input())
  uvw = map(
    int,
    sys.stdin.read().split(),
  )
  uf = UnionFind(n)
  tot = 0
  uvw = sorted(
    list(zip(*[uvw] * 3)),
    key=lambda x: x[2],
  )
  for u, v, w in uvw:
    u -= 1; v -= 1
    tot += uf.size(u) * uf.size(v) * w
    uf.unite(u, v)
  print(tot)


main()
