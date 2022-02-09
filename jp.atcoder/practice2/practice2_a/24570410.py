import typing
import dataclasses


@dataclasses.dataclass
class Node():
  parent: int
  size: int = 1
  rank: int = 0



class UnionFind():

  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [
      Node(i) for i in range(n)
    ]


  def find(
    self,
    u: int,
  ) -> int:
    a = self.__a
    pu = a[u].parent
    if pu == u: return u
    pu = self.find(pu)
    a[u].parent = pu
    return pu


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return
    a = self.__a
    if a[u].size < a[v].size:
      u, v = v, u
    a[u].size += a[v].size
    a[v].parent = u


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
