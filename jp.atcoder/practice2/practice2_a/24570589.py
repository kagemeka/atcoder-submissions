import typing



class UnionFind():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [-1] * n


  def find(
    self,
    u: int,
  ) -> int:
    a = self.__a
    au = a[u]
    if au < 0: return u
    au = self.find(au)
    a[u] = au
    return au


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return
    a = self.__a
    if a[u] > a[v]: u, v = v, u
    a[u] += a[v]
    a[v] = u


  def same(
    self,
    u: int,
    v: int,
  ) -> bool:
    u = self.find(u)
    v = self.find(v)
    return u == v


import sys

def main() -> typing.NoReturn:
  n, q = map(
    int, input().split(),
  )
  uf = UnionFind(n)
  q = map(
    int,
    sys.stdin.read().split(),
  )
  for t, u, v in zip(*[q] * 3):
    if t == 0:
      uf.unite(u, v)
      continue
    print(uf.same(u, v) * 1)


main()
