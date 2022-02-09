import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
from scipy import optimize
# from numba import jit
from heapq import heappush, heappop
from bisect import bisect_left as bi_l, bisect_right as bi_r
from collections import deque, Counter, defaultdict
from itertools import combinations, product, accumulate
import string
import math
inf = float('inf')
from functools import lru_cache
sys.setrecursionlimit(10**7)
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
  def gcd(self, a, b): return self.gcd(b, a%b) if b else abs(a)
  def lcm(self, a, b): return abs(a // self.gcd(a, b) * b)
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

  def mod_choose(self, n, r):
    return self.fac[n]*self.ifac[r]%self.mod*self.ifac[n-r]%self.mod

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
    h1, h2 = map(int, sys.stdin.read().split()); print(h1-h2)
  def B(): pass
  def C(): pass
  def D(): pass

class ABC002():
  def A():
    print(max(map(int, sys.stdin.readline().split())))
  def B():
    vowels = set('aeiou')
    print(''.join([c for c in sys.stdin.readline().rstrip() if c not in vowels]))
  def C():
    def triangle_area(x0, y0, x1, y1, x2, y2):
      x1 -= x0; x2 -= x0; y1 -= y0; y2 -= y0;
      return abs(x1*y2 - x2*y1) / 2
    print(triangle_area(*map(int, sys.stdin.readline().split())))
  def D():
    n, m = map(int, sys.stdin.readline().split())
    edges = set((x-1, y-1) for x, y in zip(*[map(int, sys.stdin.read().split())]*2))
    print(max(len(s) for i in range(1, 1<<n) for s in [[j for j in range(n) if i>>j&1]] if all((x, y) in edges for x, y in combinations(s, 2))))

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
  def D():
    ng = set([4, 9])
    def count(d):
      return d if d<=4 else d-1
    def f(n):
      x = [int(d) for d in str(n)]
      flg = True
      dp = 0
      for d in x:
        dp = dp*8 + flg*count(d)
        if d in ng: flg = False
      return n-(dp+flg)
    a, b = map(int, sys.stdin.readline().split())
    print(f(b) - f(a-1))

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

class ABC032():
  def A():
    a, b, n = map(int, sys.stdin.read().split())
    l = NumberTheory().lcm(a, b)
    print((n+l-1)//l*l)
  def B():
    s, k = sys.stdin.read().split()
    k = int(k)
    res = set()
    for i in range(len(s)-k+1):
      res.add(s[i:i+k])
    print(len(res))
  def C():
    n, k, *s = map(int, sys.stdin.read().split())
    if 0 in s: print(n); return
    s += [inf]
    res = 0
    l = r = 0
    tmp = 1
    while r <= n:
      tmp *= s[r]
      while tmp > k:
        res = max(res, r-l)
        tmp //= s[l]
        l += 1
      r += 1
    print(res)
  def D(): pass

class ABC033():
  def A():
    n = set(sys.stdin.readline().rstrip())
    print('SAME' if len(n)==1 else 'DIFFERENT')
  def B():
    n = int(sys.stdin.readline().rstrip())
    res = dict()
    for _ in range(n):
      s, p = sys.stdin.readline().split()
      p = int(p)
      res[s] = p
    tot = sum(res.values())
    for s, p in res.items():
      if p > tot/2:
        print(s)
        return
    print('atcoder')
  def C():
    s = sys.stdin.readline().rstrip()
    res = sum(not '0' in f for f in s.split('+'))
    print(res)
  def D(): pass

class ABC034():
  def A():
    x, y = map(int, sys.stdin.readline().split())
    print('Better' if y>x else 'Worse')
  def B():
    n = int(sys.stdin.readline().rstrip())
    print(n+1 if n&1 else n-1)
  def C():
    h, w = map(int, sys.stdin.read().split())
    combinatorics = Combinatorics(n=2*10**5, numpy=True, mod=MOD)
    print(combinatorics.mod_choose(h+w-2, h-1))
  def D():
    n, k, *wp = map(int, sys.stdin.read().split())
    w, p = np.array(wp).reshape(-1, 2).T
    def f(x):
      return np.sort(w*(p-x))[-k:].sum()
    print(optimize.bisect(f, 0, 100))

class ABC035():
  def A():
    w, h = map(int, sys.stdin.readline().split())
    print('4:3' if 4*h==3*w else '16:9')
  def B():
    s, t = sys.stdin.read().split()
    y = 0
    x = 0
    z = 0
    for c in s:
      if c == '?': z += 1
      elif c == 'L': x -= 1
      elif c == 'R': x += 1
      elif c == 'D': y -= 1
      elif c == 'U': y += 1
    d = abs(y)+abs(x)
    if t == '1':
      print(d+z)
    else:
      print(max(d-z, (d-z)&1))
  def C():
    n, q, *lr = map(int, sys.stdin.read().split())
    l, r = np.array(lr).reshape(q, 2).T
    res = np.zeros(n+1, dtype=int)
    np.add.at(res, l-1, 1)
    np.subtract.at(res, r, 1)
    np.cumsum(res, out=res)
    res = res&1
    print(''.join(map(str, res[:-1])))
  def D():
    n, m, t = map(int, sys.stdin.readline().split())
    point = np.array(sys.stdin.readline().split(), dtype=int)
    a, b, c = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(m, 3).T
    a -= 1; b -= 1
    d_1 = shortest_path(csr_matrix((c, (a, b)), (n, n)), method='D', directed=True, indices=0)
    d_2 = shortest_path(csr_matrix((c, (b, a)), (n, n)), method='D', directed=True, indices=0)
    print(int(np.amax((t-(d_1+d_2))*point)))

class ABC036():
  def A():
    a, b = map(int, sys.stdin.readline().split())
    print((b+a-1)//a)
  def B():
    n, *s = sys.stdin.read().split()
    n = int(n)
    for j in range(n):
      row = ''
      for i in range(n-1, -1, -1):
        row += s[i][j]
      print(row)
  def C():
    n, *a = map(int, sys.stdin.read().split())
    b = [None]*n
    prev = None
    j = -1
    for i, x in sorted(enumerate(a), key=lambda x: x[1]):
      if x != prev: j += 1
      b[i] = j
      prev = x
    print(*b, sep='\n')
  def D():
    n, *ab = map(int, sys.stdin.read().split())
    edges = [[] for _ in range(n)]
    for a, b in zip(*[iter(ab)]*2):
      a -= 1; b -= 1
      edges[a].append(b)
      edges[b].append(a)
    parent = [None]*n
    def count(u):
      black, white = 1, 1
      for v in edges[u]:
        if v == parent[u]: continue
        parent[v] = u
        b, w = count(v)
        black *= w; black %= MOD
        white *= (b+w)%MOD; white %= MOD
      return black, white
    print(sum(count(0))%MOD)

class ABC037():
  def A():
    a, b, c = map(int, sys.stdin.readline().split())
    print(c//min(a, b))
  def B():
    n, q, *lrt = map(int, sys.stdin.read().split())
    a = np.zeros(n, dtype=int)
    for l, r, t in zip(*[iter(lrt)]*3):
      a[l-1:r] = t
    print(*a, sep='\n')
  def C():
    n, k, *a = map(int, sys.stdin.read().split())
    a = np.array([0]+a)
    np.cumsum(a, out=a)
    s = (a[k:] - a[:-k]).sum()
    print(s)
  def D():
    h, w = map(int, sys.stdin.readline().split())
    a = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]
    dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    path = [[None]*w for _ in range(h)]
    def paths(i, j):
      if path[i][j]: return path[i][j]
      val = a[i][j]
      cnt = 1
      for dy, dx in dyx:
        y = i+dy; x = j+dx
        if 0<=y<h and 0<=x<w and a[y][x]<val:
          cnt += paths(y, x)
          cnt %= MOD
      path[i][j] = cnt
      return cnt
    tot = 0
    for i in range(h):
      for j in range(w):
        tot += paths(i, j)
        tot %= MOD
    print(tot)

class ABC038():
  def A():
    s = sys.stdin.readline().rstrip()
    print('YES' if s[-1]=='T' else 'NO')
  def B():
    a, b, c, d = map(int, sys.stdin.read().split())
    print('YES' if a==c or b==c or a==d or b==d else 'NO')
  def C():
    n, *a = map(int, sys.stdin.read().split())
    a += [-1]
    cnt = n
    tmp = 1
    for i in range(n):
      if a[i+1] > a[i]:
        tmp += 1
      else:
        cnt += tmp*(tmp-1)//2
        tmp = 1
    print(cnt)
  def D():
    n, *wh = map(int, sys.stdin.read().split())
    wh = sorted(zip(*[iter(wh)]*2), key=lambda x: (-x[0], x[1]))
    w = [x[1] for x in wh][::-1]
    res = [inf] * n
    for x in w:
      res[bi_l(res, x)] = x
    print(bi_l(res, inf))

class ABC039():
  def A():
    a, b, c = map(int, sys.stdin.readline().split())
    print((a*b+b*c+c*a)*2)
  def B():
    x = int(sys.stdin.readline().rstrip())
    for n in range(1, int(x**0.5)+1):
      if pow(n, 4)==x:
        print(n); return
  def C():
    board = 'WBWBWWBWBWBW' * 3
    convert = 'Do, *, Re, *, Mi, Fa, *, So, *, La, *, Si'.split(', ')
    s = sys.stdin.readline().rstrip()
    print(convert[board.index(s)])
  def D():
    h, w = map(int, sys.stdin.readline().split())
    s = sys.stdin.read().split()
    dyx = list(product((-1, 0, 1), repeat=2))
    black_certain = set()
    black_before = set()
    for i in range(h):
      for j in range(w):
        black_cand = set()
        for dy, dx in dyx:
          y = i+dy; x = j+dx
          if y<0 or y>=h or x<0 or x>=w: continue
          if s[y][x] == '.': break
          black_cand.add((y, x))
        else:
          black_before.add((i, j))
          black_certain |= black_cand
    for i in range(h):
      for j in range(w):
        if s[i][j]=='#' and not (i, j) in black_certain:
          print('impossible')
          return
    print('possible')
    for i in range(h):
      row = ''
      for j in range(w):
        row += '#' if (i, j) in black_before else '.'
      print(''.join(row))

class ABC040():
  def A():
    n, x = map(int, sys.stdin.readline().split())
    print(min(x-1, n-x))
  def B():
    n = int(sys.stdin.readline().rstrip())
    res = inf
    for i in range(1, int(n**.5)+1):
      res = min(res, n//i-i+n%i)
    print(res)
  def C():
    n, *h = map(int, sys.stdin.read().split())
    h = [h[0]]+h
    cost = [None] * (n+1); cost[0] = cost[1] = 0
    for i in range(2, n+1):
      cost[i] = min(
        cost[i-2] + abs(h[i]-h[i-2]),
        cost[i-1] + abs(h[i]-h[i-1])
      )
    print(cost[n])
  def D():
    n, m = map(int, sys.stdin.readline().split())
    uf = UnionFind(n=n)
    queue = []
    for _ in range(m):
      a, b, y = map(int, sys.stdin.readline().split())
      heappush(queue, (-(2*y), a-1, b-1))
    q = int(sys.stdin.readline().rstrip())
    for i in range(q):
      v, y = map(int, sys.stdin.readline().split())
      heappush(queue, (-(2*y+1), v-1, i))
    res = [None] * q
    while queue:
      y, i, j = heappop(queue)
      if y&1:
        res[j] = uf.size[uf.find_root(i)]
      else:
        uf.unite(i, j)
    print(*res, sep='\n')

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
  def D():
    h, w, a, b = map(int, sys.stdin.read().split())
    combinatorics = Combinatorics(n=2*10**5, mod=MOD, numpy=True)
    tot = combinatorics.mod_choose(h+w-2, h-1)
    i = np.arange(h-a, h)
    ng = np.sum(combinatorics.mod_choose(i+b-1, i) * combinatorics.mod_choose(h-i+w-b-2, h-1-i) % MOD)
    tot -= ng; tot %= MOD
    print(tot)

class ABC043():
  def A():
    n = int(sys.stdin.readline().rstrip())
    print((1+n)*n//2)
  def B():
    s = sys.stdin.readline().rstrip()
    t = ''
    for c in s:
      if c == 'B': t = t[:-1]
      else: t += c
    print(t)
  def C():
    n, *a = map(int, sys.stdin.read().split())
    a = np.array(a)
    x = np.around(a.sum()/n).astype(int)
    print(np.sum((a-x)**2))
  def D():
    s = sys.stdin.readline().rstrip()
    n = len(s)
    for i in range(n-1):
      if s[i] == s[i+1]:
        print(i+1, i+2); return
    for i in range(n-2):
      if s[i] == s[i+2]:
        print(i+1, i+3); return
    print(-1, -1)

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
    m = 2*10**5
    infants = [[] for _ in range(m)]
    highest_rate = [None] * m
    where = [None] * n
    rate = [None] * n

    def entry(i, k):
      where[i] = k
      while infants[k]:
        r, j = heappop(infants[k])
        if where[j] != k or j == i: continue
        if rate[i] >= -r:
          highest_rate[k] = rate[i]
          heappush(queue, (rate[i], k, i))
        heappush(infants[k], (r, j))
        break
      else:
        highest_rate[k] = rate[i]
        heappush(queue, (rate[i], k, i))
      heappush(infants[k], (-rate[i], i))

    def transfer(i, k):
      now = where[i]
      while infants[now]:
        r, j = heappop(infants[now])
        if where[j] != now or j == i: continue
        if highest_rate[now] != -r:
          highest_rate[now] = -r
          heappush(queue, (-r, now, j))
        heappush(infants[now], (r, j))
        break
      else:
        highest_rate[now] = None
      entry(i, k)

    def inquire():
      while True:
        r, k, i = heappop(queue)
        if where[i] != k or r != highest_rate[k]: continue
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
    res = ''.join([chr(ord('a')+d) for d in NumberTheory.base_convert(n, 26)][::-1])
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
  def A():
    a = int(sys.stdin.readline().rstrip())
    print(a*(1+a+a**2))
  def B():
    s, t = sys.stdin.read().split()
    print(sum(s[i]!=t[i] for i in range(len(s))))
  def C():
    n, m, k = map(int, sys.stdin.readline().split())
    *a, = [int(x) for x in sys.stdin.readline().split()]
    *b, = [int(x) for x in sys.stdin.readline().split()]
    a = [0]+a
    *sa, = accumulate(a)
    *sb, = accumulate(b)
    res = 0
    for i in range(n+1):
      r = k - sa[i]
      if r < 0: break
      j = bi_r(sb, r)
      res = max(res, i+j)
    print(res)

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

class MSolutions2020():
  def A():
    x = int(sys.stdin.readline().rstrip())
    x -= 400
    print(8-x//200)
  def B():
    r, g, b, k = map(int, sys.stdin.read().split())
    while k and g <= r:
      g *= 2
      k -= 1
    while k and b <= g:
      b *= 2
      k -= 1
    print('Yes' if r < g < b else 'No')
  def C():
    n, k, *a = map(int, sys.stdin.read().split())
    for i in range(k, n):
      print('Yes' if a[i] > a[i-k] else 'No')
  def D():
    n, *a = map(int, sys.stdin.read().split())
    a += [-1]
    m = 1000
    s = 0
    for i in range(n):
      if a[i+1] == a[i]: continue
      elif a[i+1] > a[i]:
        cnt = m//a[i]
        m -= a[i]*cnt
        s += cnt
      else:
        m += a[i]*s
        s = 0
    print(m)

  def E(): pass
  def F(): pass

if __name__ == '__main__':
  # MSolutions2020.D()
  ABC002.D()
