import typing
import sys



class UnionFind:
  def __init__(
    self,
    n: int,
  ):
    self.__p = list(range(n))
    self.__r = [0] * n
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
    p, s, r = self.__p, self.__s, self.__r
    if r[u] < r[v]: u, v = v, u
    p[v] = u
    s[u] += s[v]
    r[u] = max(r[u], r[v] + 1)


  def same(
    self,
    u: int,
    v: int,
  ) -> bool:
    return self.find(u) == self.find(v)


  def size(
    self,
    u: int,
  ) -> int:
    u = self.find(u)
    return self.__s[u]


  def groups(self) -> typing.List[
    typing.List[int]
  ]:
    n = len(self.__r)
    g = [[] for _ in range(n)]
    for u in range(n):
      g[self.find(u)].append(u)
    return [x for x in g if x]



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
