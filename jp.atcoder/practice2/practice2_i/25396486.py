import typing



class SAIS():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    self.__a = a
    self.__preprocess()
    self.__induce()
    self.__correct_lms_order()
    self.__induce()
    return self.__sa[1:]


  def __correct_lms_order(
    self,
  ) -> typing.NoReturn:
    is_lms = self.__is_lms
    lms_idx = [i for i in self.__sa if is_lms[i]]
    a = self.__a
    n = len(a)
    m = len(lms_idx)
    na = [-1] * n
    na[-1] = i = 1
    for j in range(m - 1):
      j, k = lms_idx[j], lms_idx[j + 1]
      for d in range(n):
        j_is_lms = is_lms[j + d]
        k_is_lms = is_lms[k + d]
        if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms:
          i += 1; break
        if d > 0 and j_is_lms | k_is_lms: break
      na[k] = i
    na = [i for i in na if i > 0]
    if i == m:
      lms_order = [-1] * m
      for i, j in enumerate(na):
        lms_order[j - 1] = i
    else:
      lms_order = SAIS()(na)
    self.__lms = [self.__lms[i] for i in lms_order]


  def __induce(
    self,
  ) -> typing.NoReturn:
    self.__sa = [-1] * len(self.__a)
    self.__set_lms()
    self.__induce_l()
    self.__induce_s()


  def __induce_l(
    self,
  ) -> typing.NoReturn:
    sa = self.__sa
    sa_idx = self.__b.copy()
    s = 0
    for i in range(self.__m):
      s, sa_idx[i] = s + sa_idx[i], s
    for i in range(len(sa)):
      i = sa[i] - 1
      if i < 0 or self.__is_s[i]: continue
      x = self.__a[i]
      sa[sa_idx[x]] = i
      sa_idx[x] += 1


  def __induce_s(
    self,
  ) -> typing.NoReturn:
    sa = self.__sa
    sa_idx = self.__b.copy()
    for i in range(self.__m - 1):
      sa_idx[i + 1] += sa_idx[i]
    for i in range(len(sa) - 1, -1, -1):
      i = sa[i] - 1
      if i < 0 or not self.__is_s[i]: continue
      x = self.__a[i]
      sa_idx[x] -= 1
      sa[sa_idx[x]] = i


  def __make_bucket(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    b = [0] * self.__m
    for x in a: b[x] += 1
    self.__b = b


  def __preprocess(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    if min(a) <= 0:
      a = [x + 1 for x in a]
    assert all(x > 0 for x in a)
    self.__m = max(a) + 1
    a = a + [0]
    n = len(a)
    self.__a = a

    is_s = [True] * n
    for i in range(n - 2, -1, -1):
      is_s[i] = (
        is_s[i + 1] if a[i] == a[i + 1] else
        a[i] < a[i + 1]
      )

    is_lms = [is_s[i] and not is_s[i - 1] for i in range(n)]
    lms = [i for i in range(n) if is_lms[i]]

    self.__is_s = is_s
    self.__is_lms = is_lms
    self.__lms = lms
    self.__make_bucket()


  def __set_lms(
    self,
  ) -> typing.NoReturn:
    sa_idx = self.__b.copy()
    for i in range(self.__m - 1):
      sa_idx[i + 1] += sa_idx[i]
    for i in self.__lms[::-1]:
      x = self.__a[i]
      sa_idx[x] -= 1
      self.__sa[sa_idx[x]] = i



class LCPKasai():
  def __call__(
    self,
    a: typing.List[int],
    sa: typing.List[int],
  ) -> typing.List[int]:
    n = len(a)
    assert n > 0 and len(sa) == n
    rank = [-1] * n
    for i, x in enumerate(sa): rank[x] = i
    h, l = [0] * (n - 1), 0
    for i in range(n):
      if l > 0: l -= 1
      r = rank[i]
      if r == n - 1: continue
      j = sa[r + 1]
      while i + l < n and j + l < n:
        if a[i + l] != a[j + l]: break
        l += 1
      h[r] = l
    return h



def solve(
  a: typing.List[int],
) -> typing.NoReturn:
  sa = SAIS()(a)
  lcp = LCPKasai()(a, sa)
  n = len(a)
  s = n * (n + 1) // 2
  print(s - sum(lcp))


def main() -> typing.NoReturn:
  s = [ord(x) - ord('a') + 1 for x in input()]
  solve(s)


main()
