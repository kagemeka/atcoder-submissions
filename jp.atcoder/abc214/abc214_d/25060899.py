import typing
import sys



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
    if a[u] > a[v]: u, v = v, u
    a[u] += a[v]
    a[v] = u


  def size(
    self,
    u: int,
  ) -> int:
    return -self.__a[self.find(u)]



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
