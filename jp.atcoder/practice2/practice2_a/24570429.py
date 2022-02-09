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
