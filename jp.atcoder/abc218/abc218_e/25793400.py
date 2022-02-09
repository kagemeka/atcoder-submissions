import typing



class UnionFind():
  def __init__(self, n: int) -> typing.NoReturn:
    self.__a = [-1] * n


  def find(self, u: int) -> int:
    a = self.__a
    if a[u] < 0: return u
    a[u] = self.find(a[u])
    return a[u]


  def unite(self, u: int, v: int) -> typing.NoReturn:
    u, v = self.find(u), self.find(v)
    if u == v: return
    a = self.__a
    if a[u] > a[v]: u, v = v, u
    a[u] += a[v]
    a[v] = u



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abc = [
    tuple(map(int, input().split()))
    for _ in range(m)
  ]
  abc.sort(key=lambda x: x[2])
  uf = UnionFind(n)

  s = 0
  for a, b, c in abc:
    a -= 1; b -= 1
    if c >= 0 and uf.find(a) == uf.find(b):
      s += c
      continue
    uf.unite(a, b)

  print(s)


main()
