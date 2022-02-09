import sys
import numpy as np
from heapq import heappush, heappop
from bisect import bisect_left as bi_l, bisect_right as bi_r
from collections import deque, Counter, defaultdict
from itertools import combinations, product
import string
inf = float('inf')
MOD = 10**9+7
# MOD = 998244353


class NumberTheory():
  def __init__(self, n=2*10**6, numpy=True):
    self.n = n
    self.np_flg = numpy
    self.is_prime_number, self.prime_numbers = self.sieve_of_eratosthenes(n)

  def sieve_of_eratosthenes(self, n):
    if self.np_flg:
      sieve = np.ones(n+1, dtype=np.int64); sieve[:2] = 0
      for i in range(2, int(n**.5)+1):
        if sieve[i]: sieve[i*2::i] = 0
      prime_numbers = np.flatnonzero(sieve)
    else:
      sieve = [1] * (n+1); sieve[0] = sieve[1] = 0
      for i in range(2, int(n**.5)+1):
        if not sieve[i]: continue
        for j in range(i*2, n+1, i): sieve[j] = 0
      prime_numbers = [i for i in range(2, n+1) if sieve[i]]
    return sieve, prime_numbers

  def prime_factorize(self, n):
    res = dict()
    if n < 2: return res
    border = int(n**.5)
    for p in self.prime_numbers:
      if p > border: break
      while n % p == 0: res[p] = res.get(p, 0)+1; n //= p
      if n == 1: return res
    res[n] = 1; return res

  def prime_factorize_factorial(self, n):
    res = dict()
    for i in range(2, n+1):
      for p, c in self.prime_factorize(i).items(): res[p] = res.get(p, 0)+c
    return res

  @staticmethod
  def gcd(a, b): return gcd(b, a%b) if b else abs(a)

  @staticmethod
  def lcm(a, b): return abs(a // gcd(a, b) * b)

  @staticmethod
  def find_divisors(n):
    divisors = []
    for i in range(1, int(n**.5)+1):
      if n%i: continue
      divisors.append(i)
      j = n // i
      if j != i: divisors.append(j)
    return divisors

  @staticmethod
  def base_convert(n, b):
    if not n: return [0]
    res = []
    while n:
      n, r = divmod(n, b)
      if r < 0: n += 1; r -= b
      res.append(r)
    return res


class UnionFind():
  def __init__(self, n=10**6):
    self.root = list(range(n))
    self.height = [0] * n
    self.size = [1] * n

  def find_root(self, u):
    if self.root[u] == u: return u
    self.root[u] = self.find_root(self.root[u])
    return self.root[u]

  def unite(self, u, v):
    ru = self.find_root(u)
    rv = self.find_root(v)
    if ru == rv: return
    hu = self.height[ru]
    hv = self.height[rv]
    if hu >= hv:
      self.root[rv] = ru
      self.size[ru] += self.size[rv]
      self.height[ru] = max(hu, hv+1)
    else:
      self.root[ru] = rv
      self.size[rv] += self.size[ru]


class Combinatorics():
  def __init__(self, N=10**9, n=10**6, mod=10**9+7, numpy=True):
    self.mod = mod
    self.nCr = dict()
    self.np_flg=numpy
    self.make_mod_tables(N, n)

  sys.setrecursionlimit(10**6)
  def choose(self, n, r, mod=None): # no mod, or mod ≠ prime
    if r > n or r < 0: return 0
    if r == 0: return 1
    if (n, r) in self.nCr: return self.nCr[(n, r)]
    if not mod:
      self.nCr[(n, r)] = (self.choose(n-1, r) + self.choose(n-1, r-1))
    else:
      self.nCr[(n, r)] = (self.choose(n-1, r, mod) + self.choose(n-1, r-1, mod)) % mod
    return self.nCr[(n,r)]

  def cumprod(self, a):
    p = self.mod
    l = len(a); sql = int(np.sqrt(l)+1)
    a = np.resize(a, sql**2).reshape(sql, sql)
    for i in range(sql-1): a[:, i+1] *= a[:, i]; a[:, i+1] %= p
    for i in range(sql-1): a[i+1] *= a[i, -1]; a[i+1] %= p
    return np.ravel(a)[:l]

  def make_mod_tables(self, N, n):
    p = self.mod
    if self.np_flg:
      fac = np.arange(n+1); fac[0] = 1; fac = self.cumprod(fac)
      ifac = np.arange(n+1, 0, -1); ifac[0] = pow(int(fac[-1]), p-2, p)
      ifac = self.cumprod(ifac)[n::-1]
      n_choose = np.arange(N+1, N-n, -1); n_choose[0] = 1;
      n_choose[1:] = self.cumprod(n_choose[1:])*ifac[1:n+1]%p
    else:
      fac = [None]*(n+1); fac[0] = 1
      for i in range(n): fac[i+1] = fac[i]*(i+1)%p
      ifac = [None]*(n+1); ifac[n] = pow(fac[n], p-2, p)
      for i in range(n, 0, -1): ifac[i-1] = ifac[i]*i%p
      n_choose = [None] * (n+1); n_choose[0] = 1
      for i in range(n): n_choose[i+1] = n_choose[i]*(N-i)%p
      for i in range(n+1): n_choose[i] = n_choose[i]*ifac[i]%p
    self.fac, self.ifac, self.mod_n_choose = fac, ifac, n_choose


def z_algorithm(s):
  n = len(s)
  a = [0] * n; a[0] = n
  l = r = -1
  for i in range(1, n):
    if r >= i: a[i] = min(a[i-l], r-i)
    while i + a[i] < n and s[i+a[i]] == s[a[i]]: a[i] += 1
    if i+a[i] >= r: l, r = i, i+a[i]
  return a


class ABC001():
  def A():
    h1, h2 = map(int, sys.stdin.read().split())
    print(h1-h2)

  def B(): pass
  def C(): pass
  def D(): pass


class ABC002():
  def A():
    x, y = map(int, sys.stdin.readline().split())
    print(max(x, y))

  def B():
    vowels = set('aeiou')
    s = sys.stdin.readline().rstrip()
    t = ''
    for c in s:
      if c in vowels: continue
      t += c
    print(t)

  def C():
    *coords, = map(int, sys.stdin.readline().split())
    def triangle_area(x0, y0, x1, y1, x2, y2):
      x1 -= x0; x2 -= x0; y1 -= y0; y2 -= y0;
      return abs(x1*y2 - x2*y1) / 2
    print(triangle_area(*coords))

  def D():
    n, m = map(int, sys.stdin.readline().split())
    edges = set()
    for _ in range(m):
      x, y = map(int, sys.stdin.readline().split())
      x -= 1; y -= 1
      edges.add((x, y))
    cand = []
    for i in range(1, 1<<n):
      s = [j for j in range(n) if i>>j & 1]
      for x, y in combinations(s, 2):
        if (x, y) not in edges: break
      else:
        cand.append(len(s))
    print(max(cand))


class ABC003():
  def A():
    n = int(sys.stdin.readline().rstrip())
    print((n+1)*5000)

  def B():
    atcoder = set('atcoder')
    s, t = sys.stdin.read().split()
    for i in range(len(s)):
      if s[i] == t[i]: continue
      if s[i] == '@' and t[i] in atcoder: continue
      if t[i] == '@' and s[i] in atcoder: continue
      print('You will lose')
      return
    print('You can win')

  def C():
    n, k, *r = map(int, sys.stdin.read().split())
    res = 0
    for x in sorted(r)[-k:]:
      res = (res+x) / 2
    print(res)

  def D(): pass


class ABC004():
  def A():
    print(int(sys.stdin.readline().rstrip())*2)

  def B():
    c = [sys.stdin.readline().rstrip() for _ in range(4)]
    for l in c[::-1]:
      print(l[::-1])

  def C():
    n = int(sys.stdin.readline().rstrip())
    n %= 30
    res = list(range(1, 7))
    for i in range(n):
      i %= 5
      res[i], res[i+1] = res[i+1], res[i]
    print(''.join(map(str, res)))

  def D(): pass


class ABC005():
  def A():
    x, y = map(int, sys.stdin.readline().split())
    print(y//x)

  def B():
    n, *t = map(int, sys.stdin.read().split())
    print(min(t))

  def C():
    t = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().split()]
    m = int(sys.stdin.readline().rstrip())
    b = [int(x) for x in sys.stdin.readline().split()]
    i = 0
    for p in b:
      if i == n: print('no'); return
      while p-a[i] > t:
        i += 1
        if i == n: print('no'); return
      if a[i] > p: print('no'); return
      i += 1
    print('yes')

  def D():
    n = int(sys.stdin.readline().rstrip())
    d = np.array([sys.stdin.readline().split() for _ in range(n)], np.int64)
    s = d.cumsum(axis=0).cumsum(axis=1)
    s = np.pad(s, 1)
    max_del = np.zeros((n+1, n+1), dtype=np.int64)
    for y in range(1, n+1):
      for x in range(1, n+1):
        max_del[y, x] = np.amax(s[y:n+1, x:n+1] - s[0:n-y+1, x:n+1] - s[y:n+1, 0:n-x+1] + s[0:n-y+1, 0:n-x+1])
    res = np.arange(n**2+1)[:, None]
    i = np.arange(1, n+1)
    res = max_del[i, np.minimum(res//i, n)].max(axis=1)
    q = int(sys.stdin.readline().rstrip())
    p = np.array(sys.stdin.read().split(), dtype=np.int64)
    print(*res[p], sep='\n')


class ABC006():
  def A():
    n = sys.stdin.readline().rstrip()
    if '3' in n: print('YES')
    elif int(n)%3 == 0: print('YES')
    else: print('NO')

  def B():
    mod = 10007
    t = [0, 0, 1]
    for _ in range(1001001):
      t.append(t[-1]+t[-2]+t[-3]); t[-1] %= mod
    n = int(sys.stdin.readline().rstrip())
    print(t[n-1])

  def C():
    n, m = map(int, sys.stdin.readline().split())
    cnt = [0, 0, 0]
    if m == 1: cnt = [-1, -1, -1]
    else:
      if m & 1: m -= 3; cnt[1] += 1; n -= 1
      cnt[2] = m//2 - n
      cnt[0] = n - cnt[2]
    if cnt[0]<0 or cnt[1]<0 or cnt[2]<0: print(-1, -1, -1)
    else: print(*cnt, sep=' ')

  def D():
    n, *c = map(int, sys.stdin.read().split())
    lis = [inf]*n
    for x in c: lis[bi_l(lis, x)] = x
    print(n - bi_l(lis, inf))


class ABC007():
  def A():
    n = int(sys.stdin.readline().rstrip())
    print(n-1)

  def B():
    s = sys.stdin.readline().rstrip()
    if s == 'a': print(-1)
    else: print('a')

  def C():
    r, c = map(int, sys.stdin.readline().split())
    sy, sx = map(int, sys.stdin.readline().split())
    gy, gx = map(int, sys.stdin.readline().split())
    sy -= 1; sx -=1; gy -= 1; gx -= 1
    maze = [sys.stdin.readline().rstrip() for _ in range(r)]
    queue = deque([(sy, sx)])
    dist = np.full((r, c), np.inf); dist[sy, sx] = 0
    while queue:
      y, x = queue.popleft()
      for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i += y; j += x
        if maze[i][j] == '#' or dist[i, j] != np.inf: continue
        dist[i, j] = dist[y, x] + 1
        queue.append((i, j))
    print(int(dist[gy, gx]))

  def D(): pass


class ABC008():
  def A():
    s, t = map(int, sys.stdin.readline().split())
    print(t-s+1)

  def B():
    n, *s = sys.stdin.read().split()
    res = defaultdict(int)
    for name in s: res[name] += 1
    print(sorted(res.items(), key=lambda x: x[1])[-1][0])

  def C():
    n, *a = map(int, sys.stdin.read().split())
    a = np.array(a)
    c = n - np.count_nonzero(a[:, None]%a, axis=1)
    print(np.sum((c+1)//2/c))

  def D(): pass

class ABC009():
  def A():
    n = int(sys.stdin.readline().rstrip())
    print((n+1)//2)

  def B():
    n, *a = map(int, sys.stdin.read().split())
    print(sorted(set(a))[-2])

  def C():
    n, k = map(int, sys.stdin.readline().split())
    s = list(sys.stdin.readline().rstrip())
    cost = [1]*n
    r = k
    for i in range(n-1):
      q = []
      for j in range(i+1, n):
        if s[j] < s[i] and cost[i]+cost[j] <= r:
          heappush(q, (s[j], cost[i]+cost[j], -j))
      if not q: continue
      _, c, j = heappop(q); j = -j
      s[i], s[j] = s[j], s[i]
      r -= c
      cost[i] = cost[j] = 0
    print(''.join(s))

  def D(): pass


class ABC010():
  def A():
    print(sys.stdin.readline().rstrip()+'pp')
  def B():
    n, *a = map(int, sys.stdin.read().split())
    tot = 0
    for x in a:
      c = 0
      while x%2==0 or x%3==2:
        x -= 1
        c += 1
      tot += c
    print(tot)

  def C():
    sx, sy, gx, gy, t, v, n, *xy = map(int, sys.stdin.read().split())
    x, y = np.array(xy).reshape(-1, 2).T
    def dist(x1, y1, x2, y2):
      return np.sqrt((x2-x1)**2 + (y2-y1)**2)
    ans = 'YES' if (dist(sx, sy, x, y)+dist(x, y, gx, gy) <= v*t).any() else 'NO'
    print(ans)

  def D(): pass

class ABC011():
  def A():
    n = int(sys.stdin.readline().rstrip())
    print(n%12+1)

  def B():
    s = sys.stdin.readline().rstrip()
    print(s[0].upper()+s[1:].lower())

  def C():
    n, *ng = map(int, sys.stdin.read().split())
    ng = set(ng)
    if n in ng: print('NO')
    else:
      r = 100
      while n > 0:
        if r == 0: print('NO'); return
        for i in range(3, 0, -1):
          if (n-i) in ng: continue
          n -= i
          r -= 1
          break
        else: print('NO'); return
      print('YES')

  def D(): pass


class ABC041():
  def A():
    s, i = sys.stdin.read().split()
    i = int(i)
    print(s[i-1])

  def B():
    a, b, c = map(int, sys.stdin.readline().split())
    ans = a * b % MOD * c % MOD
    print(ans)

  def C():
    n, *a = map(int, sys.stdin.read().split())
    for i, h in sorted(enumerate(a), key=lambda x: -x[1]):
      print(i+1)

  def D():
    n, m, *xy = map(int, sys.stdin.read().split())
    *xy, = zip(*[iter(xy)]*2)
    edges = [0] * n
    for x, y in xy:
      x -= 1; y -= 1
      edges[x] |= 1<<y
    comb = [None] * (1<<n); comb[0] = 1
    def count(edges, bit):
      if comb[bit] is not None: return comb[bit]
      comb[bit] = 0
      for i in range(n):
        if (bit>>i) & 1 and not edges[i]:
          nxt_bit = bit & ~(1<<i)
          nxt_edges = edges.copy()
          for j in range(n):
            nxt_edges[j] &= ~(1<<i)
          cnt = count(nxt_edges, nxt_bit)
          comb[bit] += cnt
      return comb[bit]
    print(count(edges, (1<<n)-1))


class ABC042():
  def A():
    a = [int(x) for x in sys.stdin.readline().split()]
    c = Counter(a)
    print('YES' if c[5]==2 and c[7]==1 else 'NO')

  def B():
    n, l, *s = sys.stdin.read().split()
    print(''.join(sorted(s)))

  def C():
    n, k, *d = sys.stdin.read().split()
    l = len(n)
    ok = sorted(set(string.digits)-set(d))
    cand = [int(''.join(p)) for p in product(ok, repeat=l)] + [int(min(x for x in ok if x > '0')+min(ok)*l)]
    print(cand[bi_l(cand, int(n))])

  def D(): pass


class ABC170():
  def A():
    x = [int(x) for x in sys.stdin.readline().split()]
    for i in range(5):
      if x[i] != i+1:
        print(i+1)
        break

  def B():
    x, y = map(int, sys.stdin.readline().split())
    print('Yes' if 2*x <= y <= 4*x and y%2 == 0 else 'No')

  def C():
    x, n, *p = map(int, sys.stdin.read().split())
    a = list(set(range(102)) - set(p))
    a = [(abs(y-x), y) for y in a]
    print(sorted(a)[0][1])

  def D():
    n, *a = map(int, sys.stdin.read().split())
    cand = set(a)
    cnt = 0
    for x, c in sorted(Counter(a).items()):
      cnt += c == 1 and x in cand
      cand -= set(range(x*2, 10**6+1, x))
    print(cnt)

  def E():
    n, q = map(int, sys.stdin.readline().split())
    queue = []
    num_kindergarten = 2*10**5
    queue_kindergarten = [[] for _ in range(num_kindergarten)]
    highest_kindergarten = [None] * num_kindergarten
    where = [None] * n
    rate = [None] * n

    def entry(i, k):
      where[i] = k
      while queue_kindergarten[k]:
        r, j = heappop(queue_kindergarten[k])
        if where[j] != k or j == i: continue
        if rate[i] >= -r:
          highest_kindergarten[k] = rate[i]
          heappush(queue, (rate[i], k, i))
        heappush(queue_kindergarten[k], (r, j))
        break
      else:
        highest_kindergarten[k] = rate[i]
        heappush(queue, (rate[i], k, i))
      heappush(queue_kindergarten[k], (-rate[i], i))

    def transfer(i, k):
      now = where[i]
      while queue_kindergarten[now]:
        r, j = heappop(queue_kindergarten[now])
        if where[j] != now or j == i: continue
        if highest_kindergarten[now] != -r:
          highest_kindergarten[now] = -r
          heappush(queue, (-r, now, j))
        heappush(queue_kindergarten[now], (r, j))
        break
      else:
        highest_kindergarten[now] = None
      entry(i, k)

    def inquire():
      while True:
        r, k, i = heappop(queue)
        if where[i] != k or r != highest_kindergarten[k]: continue
        heappush(queue, (r, k, i))
        return r

    for i in range(n):
      a, b = map(int, sys.stdin.readline().split())
      rate[i] = a
      entry(i, b-1)
    for _ in range(q):
      c, d = map(int, sys.stdin.readline().split())
      transfer(c-1, d-1)
      print(inquire())

  def F(): pass


class ABC171():
  def A():
    c = sys.stdin.readline().rstrip()
    print('A' if c < 'a' else 'a')

  def B():
    n, k, *p = map(int, sys.stdin.read().split())
    print(sum(sorted(p)[:k]))

  def C():
    n = int(sys.stdin.readline().rstrip())
    n -= 1
    l = 1
    while True:
      if n < pow(26, l):
        break
      n -= pow(26, l)
      l += 1
    res = ''.join([chr(ord('a')+d%26) for d in NumberTheory.base_convert(n, 26)][::-1])
    res = 'a'*(l-len(res)) + res
    print(res)

  def D():
    n = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().split()]
    s = sum(a)
    cnt = Counter(a)
    q = int(sys.stdin.readline().rstrip())
    for _ in range(q):
      b, c = map(int, sys.stdin.readline().split())
      s += (c-b)*cnt[b]
      print(s)
      cnt[c] += cnt[b]; cnt[b] = 0

  def E():
    n, *a = map(int, sys.stdin.read().split())
    s = 0
    for x in a: s ^= x
    b = map(lambda x: x^s, a)
    print(*b, sep=' ')

  def F(): pass


class ABC172():
  def A(): pass
  def B(): pass
  def C(): pass
  def D(): pass
  def E(): pass
  def F(): pass


class ABC173():
  def A():
    n = int(sys.stdin.readline().rstrip())
    charge = (n+999)//1000 * 1000 - n
    print(charge)

  def B():
    n, *s = sys.stdin.read().split()
    c = Counter(s)
    for v in 'AC, WA, TLE, RE'.split(', '):
      print(f'{v} x {c[v]}')

  def C():
    h, w, k = map(int, sys.stdin.readline().split())
    c = [sys.stdin.readline().rstrip() for _ in range(h)]
    tot = 0
    for i in range(1<<h):
      for j in range(1<<w):
        cnt = 0
        for y in range(h):
          for x in range(w):
            if i>>y & 1 or j>>x & 1:
              continue
            cnt += c[y][x] ==  '#'
        tot += cnt == k
    print(tot)

  def D():
    n, *a = map(int, sys.stdin.read().split())
    a.sort(reverse=True)
    res = a[0] + sum(a[1:1+(n-2)//2])*2 + a[1+(n-2)//2]*(n & 1)
    print(res)

  def E():
    MOD = 10**9+7
    n, k, *a = map(int, sys.stdin.read().split())
    minus = [x for x in a if x < 0]
    plus = [x for x in a if x > 0]
    if len(plus) + len(minus)//2*2 >= k: # plus
      *minus, = map(abs, minus)
      minus.sort(reverse=True)
      plus.sort(reverse=True)
      cand = []
      if len(minus)&1: minus = minus[:-1]
      for i in range(0, len(minus)-1, 2):
        cand.append(minus[i]*minus[i+1]%MOD)
      if k & 1:
        res = plus[0]
        plus = plus[1:]
      else:
        res = 1
      if len(plus)&1: plus = plus[:-1]
      for i in range(0, len(plus)-1, 2):
        cand.append(plus[i]*plus[i+1]%MOD)
      cand.sort(reverse=True)
      for x in cand[:k//2]:
        res *= x
        res %= MOD
      print(res)
    elif 0 in a:
      print(0)
    else:
      cand = sorted(map(abs, a))
      res = 1
      for i in range(k):
        res *= cand[i]
        res %= MOD
      res = MOD - res
      print(res)
      pass

  def F(): pass


if __name__ == '__main__':
  ABC042.C()
