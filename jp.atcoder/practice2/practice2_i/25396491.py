import typing



class _Induce():
  def __call__(
    self,
    a: typing.List[int],
    is_s: typing.List[bool],
    lms: typing.List[int],
    bucket: typing.List[int],
  ) -> typing.List[int]:
    self.__a = a
    self.__is_s = is_s
    self.__lms = lms
    self.__b = bucket
    self.__set_lms()
    self.__induce_l()
    self.__induce_s()
    return self.__sa


  def __induce_l(self) -> typing.NoReturn:
    a, sa = self.__a, self.__sa
    idx = self.__b.copy()
    s = 0
    for i in range(len(idx)):
      s, idx[i] = s + idx[i], s
    for i in range(len(a)):
      i = sa[i] - 1
      if i < 0 or self.__is_s[i]: continue
      x = a[i]
      sa[idx[x]] = i
      idx[x] += 1


  def __induce_s(self) -> typing.NoReturn:
    a, sa = self.__a, self.__sa
    idx = self.__b.copy()
    for i in range(len(idx) - 1): idx[i + 1] += idx[i]
    for i in range(len(a) - 1, -1, -1):
      i = sa[i] - 1
      if i < 0 or not self.__is_s[i]: continue
      x = a[i]
      idx[x] -= 1
      sa[idx[x]] = i


  def __set_lms(self) -> typing.NoReturn:
    a = self.__a
    sa = [-1] * len(a)
    idx = self.__b.copy()
    for i in range(len(idx) - 1): idx[i + 1] += idx[i]
    for i in self.__lms[::-1]:
      x = a[i]
      idx[x] -= 1
      sa[idx[x]] = i
    self.__sa = sa




class SAIS():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    if min(a) <= 0:
      *a, = map(lambda x: x + 1, a)
    assert all(map(lambda x: x > 0, a))
    a = a + [0]

    st: typing.List[typing.Tuple[typing.List]] = []
    induce = _Induce()
    while True:
      is_s, is_lms, lms, b = self.__preprocess(a)
      sa = induce(a, is_s, lms, b)
      st.append((a, is_s, lms, b))
      a = self.__compute_next_array(a, sa, is_lms)
      l = len(lms)
      if max(a) < l - 1: continue
      lms_order = [-1] * l
      for i in range(l): lms_order[a[i]] = i
      break

    while st:
      a, is_s, lms, b = st.pop()
      lms = [lms[i] for i in lms_order]
      lms_order = induce(a, is_s, lms, b)

    return lms_order[1:]


  def __compute_next_array(
    self,
    a: typing.List[int],
    sa: typing.List[int],
    is_lms: typing.List[bool],
  ) -> typing.List[int]:
    n = len(a)
    lms_idx = [i for i in sa if is_lms[i]]
    l = len(lms_idx)
    na = [-1] * n
    na[-1] = i = 0
    for j in range(l - 1):
      j, k = lms_idx[j], lms_idx[j + 1]
      for d in range(n):
        j_is_lms = is_lms[j + d]
        k_is_lms = is_lms[k + d]
        if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms:
          i += 1; break
        if d > 0 and j_is_lms | k_is_lms: break
      na[k] = i
    na = [x for x in na if x >= 0]
    return na


  def __preprocess(
    self,
    a: typing.List[int],
  ) -> typing.Tuple[typing.List]:
    n = len(a)
    is_s = [True] * n
    is_s = [True] * n
    for i in range(n - 2, -1, -1):
      is_s[i] = (
        is_s[i + 1] if a[i] == a[i + 1] else
        a[i] < a[i + 1]
      )
    is_lms = [is_s[i] and not is_s[i - 1] for i in range(n)]
    lms = [i for i in range(n) if is_lms[i]]
    bucket = [0] * (max(a) + 1)
    for x in a: bucket[x] += 1
    return is_s, is_lms, lms, bucket



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
