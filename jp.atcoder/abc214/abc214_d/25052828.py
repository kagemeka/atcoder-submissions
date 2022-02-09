import typing
import sys


import typing



class UnionFind():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__p = list(range(n))
    self.__s = [1] * n
    self.__r = [0] * n


  def find(
    self,
    u: int,
  ) -> int:
    p = self.__p
    pu = p[u]
    if pu == u: return u
    pu = self.find(pu)
    p[u] = pu
    return pu


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


  def same(
    self,
    u: int,
    v: int,
  ) -> bool:
    u = self.find(u)
    v = self.find(v)
    return u == v


  def size(
    self,
    u: int,
  ) -> int:
    u = self.find(u)
    return self.__s[u]


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
    u -= 1
    v -= 1
    su = uf.size(u)
    sv = uf.size(v)
    tot += su * sv * w
    uf.unite(u, v)
  print(tot)






main()
