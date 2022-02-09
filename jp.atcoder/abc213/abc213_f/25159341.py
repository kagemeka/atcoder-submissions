import typing



class SADoubling():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    n = len(a)
    self.__n, self.__a = n, a
    self.__compress()
    self.__cnt = [0] * (n + 1)
    self.__doubling()
    return self.__sa


  def __compress(
    self,
  ) -> typing.NoReturn:
    from bisect import bisect_left
    a = self.__a
    v = sorted(set(a))
    self.__a = [bisect_left(v, x) for x in a]


  def __count_sort(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    c, n = self.__cnt, self.__n
    # assert len(a) == n
    for x in a: c[x + 1] += 1
    for i in range(n): c[i + 1] += c[i]
    idx = [0] * n
    for i in range(n):
      x = a[i]
      idx[c[x]] = i
      c[x] += 1
    for i in range(n + 1): c[i] = 0
    return idx


  def __doubling(
    self,
  ) -> typing.NoReturn:
    rank, n = self.__a, self.__n
    k = 1
    sa = list(range(n))
    while 1:
      b = [0] * n
      for i in range(n - k):
        b[i] = rank[i + k] + 1
      ord_b = self.__count_sort(b)
      a = [rank[i] for i in ord_b]
      ord_a = self.__count_sort(a)
      sa = [ord_b[i] for i in ord_a]
      c = [
        a[ord_a[i]] << 32 | b[sa[i]]
        for i in range(n)
      ]
      rank = [0] * n
      for i in range(n - 1):
        rank[sa[i + 1]] = rank[sa[i]] + (c[i + 1] > c[i])
      k *= 2
      if k >= n: break

    self.__sa = sa



class Kasai():
  def __call__(
    self,
    a: typing.List[int],
    sa: typing.List[int],
  ) -> typing.List[int]:
    n = len(a)
    assert n > 0 and len(sa) == n
    rank = [0] * n
    for i, x in enumerate(sa): rank[x] = i
    h, l = [0] * (n - 1), 0
    for i in range(n):
      if l: l -= 1
      r = rank[i]
      if r == n - 1: continue
      j = sa[r + 1]
      while i + l < n and j + l < n:
        if a[i + l] != a[j + l]: break
        l += 1
      h[r] = l
    return h



def solve(
  n: int,
  s: str,
) -> typing.NoReturn:
  s = [ord(x) for x in s]
  sa = SADoubling()(s)
  lcp = Kasai()(s, sa)

  a = list(range(n, 0, -1))
  for _ in range(2):
    st = []
    s = 0
    for i in range(n - 1):
      h, l = lcp[i], 1
      while st and st[-1][0] >= h:
        x = st.pop()
        l += x[1]
        s -= x[0] * x[1]
      s += h * l
      st.append((h, l))
      a[sa[i + 1]] += s
    sa.reverse()
    lcp.reverse()
  print(*a, sep='\n')




def main() -> typing.NoReturn:
  n = int(input())
  s = input()
  solve(n, s)


main()
