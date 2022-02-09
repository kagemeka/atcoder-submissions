import sys
from heapq import heappush, heappop 
from bisect import bisect_left as bi_l, bisect_right as bi_r
from collections import deque, Counter, defaultdict
import itertools 
import string 
import math 
from operator import xor, or_
inf = float('inf')
from functools import lru_cache, reduce
sys.setrecursionlimit(10**6)
MOD = 10**9+7
# MOD = 998244353

# global using_numpy; using_numpy = 1
# import numpy as np
# from scipy.sparse.csgraph import (
#   shortest_path, csgraph_to_dense, maximum_flow, minimum_spanning_tree
# )
# from scipy.sparse import csr_matrix
# from scipy.spatial import ConvexHull
# from scipy import optimize
# from scipy.special import comb
# from scipy.ndimage import distance_transform_cdt
# from numba import jit 
# import networkx as nx 



class Algebra:
  class Mint(int):
    def __init__(self, n, mod=MOD):
      self.value = n
      self.mod = mod

    def __str__(self): return f'{self.value}'

    def __add__(self, x): return self.__class__((self.value + x.value) % self.mod)
    def __sub__(self, x): return self.__class__((self.value - x.value) % self.mod)
    def __mul__(self, x): return self.__class__((self.value * x.value) % self.mod)
    def __pow__(self, x): return self.__class__(pow(self.value, x.value, self.mod))

    def __lt__(self, x): return self.value < x.value
    def __le__(self, x): return self.value <= x.value
    def __eq__(self, x): return self.value == x.value 
    def __ne__(self, x): return self.value != x.value
    def __gt__(self, x): return self.value > x.value
    def __ge__(self, x): return self.value >= x.value
  

  
  class SemiGroup:
    pass 
  class Monoid:
    pass
  class Group:
    pass 
  class SemiRing:
    pass
  class Ring:
    pass


  @staticmethod
  def identity(n):
    if using_numpy:
      return np.identity(n, dtype=np.int64)
    else:
      a = [[0]*n for _ in range(n)]
      for i in range(n): a[i][i] = 1
      return a

  @staticmethod
  def dot(a, b):
    if using_numpy:
      return np.dot(a, b)
    else:
      h, w, l = len(a), len(b[0]), len(b)
      assert len(a[0]) == l
      c = [[0]*w for _ in range(h)]
      for i in range(h):
        for j in range(w):
          for k in range(l):
            c[i][j] += a[i][k]*b[k][j]
      return c 
    
  @classmethod
  def matrix_pow(cls, a, n, mod=10**9+7):
    m = len(a)
    b = cls.identity(m)
    while n:
      if n&1: b = cls.dot(b, a)
      n >>= 1; a = cls.dot(a, a)
      if using_numpy:
        a %= mod; b %= mod
      else:
        for i in range(m):
          for j in range(m):
            a[i][j] %= mod
            b[i][j] %= mod
    return b

  @staticmethod
  def bitwise_dot(a, b):
    if using_numpy:
      return np.bitwise_xor.reduce(a[:,None,:] & b.T[None,:,:], axis=-1)
    else:
      h, w, l = len(a), len(b[0]), len(b)
      assert len(a[0]) == l
      c = [[0]*w for _ in range(h)]
      for i in range(h):
        for j in range(w):
          for k in range(l):
            c[i][j] ^= a[i][k]&b[k][j]
      return c 

  @classmethod
  def bitwise_mat_pow(cls, a, n):
    if n==0: return np.eye(len(a), dtype=np.uint32)*((1<<32)-1)
    res = cls.bitwise_mat_pow(a, n//2)
    res = cls.bitwise_dot(res, res)
    return cls.bitwise_dot(res, a) if n&1 else res

  class Kitamasa:
    pass


mint = Algebra.Mint


class NumberTheory:
  class PrimeNumbers: # pn
    def __init__(self, n=2*10**6):
      self.is_prime, self.prime_nums = self.find(n)
    
    def __call__(self, n): return self.is_prime[n]
    def __iter__(self): return iter(self.prime_nums)
    def __getitem__(self, key): return self.prime_nums[key]

    @staticmethod
    def find(n): # Sieve of eratosthenes
      if using_numpy:
        is_prime = np.ones(n+1, dtype=np.bool); is_prime[:2] = 0
        for i in range(2, int(n**.5)+1):
          if is_prime[i]: is_prime[i*2::i] = 0
        prime_nums = np.flatnonzero(is_prime)
      else:
        is_prime = [True]*(n+1); is_prime[0] = is_prime[1] = 0
        for i in range(2, int(n**.5)+1):
          if not is_prime[i]: continue
          for j in range(i*2, n+1, i): is_prime[j] = 0
        prime_nums = [i for i in range(2, n+1) if is_prime[i]]
      return is_prime, prime_nums 

    @lru_cache(maxsize=None)
    def factorize(self, n):
      res = defaultdict(int)
      if n < 2: return res
      for p in self:
        if p*p > n: break
        while n%p == 0: res[p] += 1; n //= p
        if n == 1: return res
      res[n] = 1; return res

    def factorize_factorial(self, n):
      res = defaultdict(int)
      for i in range(2, n+1):
        for p, c in self.factorize(i).items(): res[p] += c
      return res
  
  @classmethod
  @lru_cache(maxsize=None)
  def gcd(cls, a, b): return cls.gcd(b, a%b) if b else abs(a)
  @classmethod
  def lcm(cls, a, b): return abs(a // cls.gcd(a, b) * b)

  @staticmethod
  def find_divisors(n):
    divisors = []
    for i in range(1, int(n**.5)+1):
      if n%i: continue
      divisors.append(i)
      j = n // i
      if j != i: divisors.append(j)
    return sorted(divisors)

  @staticmethod
  def base_convert(n, b):
    if not n: return [0]
    res = []
    while n:
      n, r = divmod(n, b)
      if r < 0: n += 1; r -= b
      res.append(r)
    return res



class Combinatorics:
  def __init__(self, N=10**9, n=10**6, mod=10**9+7):
    self.mod = mod
    self.make_mod_tables(N, n)

  @classmethod
  @lru_cache(maxsize=None)
  def choose(cls, n, r, mod=None): # no mod, or mod ≠ prime
    if r > n or r < 0: return 0
    if r == 0: return 1
    res = cls.choose(n-1, r, mod) + cls.choose(n-1, r-1, mod)
    if mod: res %= mod 
    return res 
  
  def cumprod(self, a):
    p = self.mod
    l = len(a); sql = int(np.sqrt(l)+1)
    a = np.resize(a, sql**2).reshape(sql, sql)
    for i in range(sql-1): a[:, i+1] *= a[:, i]; a[:, i+1] %= p
    for i in range(sql-1): a[i+1] *= a[i, -1]; a[i+1] %= p
    return np.ravel(a)[:l]

  def make_mod_tables(self, N, n):
    p = self.mod
    if using_numpy:
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
    p = self.mod
    return self.fac[n]*self.ifac[r] % p * self.ifac[n-r] % p


  @classmethod
  def permutations(cls, a, r=None, i=0):
    a = list(a); n = len(a)
    if r is None: r = n
    res = []
    if r > n or i > r: return res
    if i == r: return [tuple(a[:r])]
    for j in range(i, n): a[i],a[j] = a[j],a[i]; res += cls.permutations(a, r, i+1)
    return res
  
  @staticmethod 
  def combinations(a, r):
    a = tuple(a)
    n = len(a)
    if r > n: return
    indices = list(range(r))
    yield a[:r]
    while True:
      for i in range(r-1, -1, -1):
        if indices[i] != i+n-r: break
      else: return
      indices[i] += 1
      for j in range(i+1, r): indices[j] = indices[j-1]+1
      yield tuple(a[i] for i in indices)




class String:
  @staticmethod
  def z_algorithm(s):
    n = len(s)
    a = [0] * n; a[0] = n
    l = r = -1
    for i in range(1, n):
      if r >= i: a[i] = min(a[i-l], r-i)
      while i + a[i] < n and s[i+a[i]] == s[a[i]]: a[i] += 1
      if i+a[i] >= r: l, r = i, i+a[i]
    return a


class GeometryTopology:
  class Graph:
    class __Edge:
      def __init__(self, weight=1, capacity=1, **args):
        self.weight = weight
        self.capacity = capacity
    
    class __Node:
      def __init__(self, **args):
        pass

    def __init__(self, n=0):
      self.__N = n
      self.__nodes = [None] * n
      self.__edges = [{} for _ in range(n)]

    def add_node(self, v, **args):
      self.__nodes[v] = self.__Node(**args)

    def add_edge(self, u, v, **args):
      # self.add_node(u); self.add_node(v)
      self.__edges[u][v] = self.__Edge(**args)

    def get_size(self): return self.__N

    def bfs(self, src=0, tree=False):
      assert 0 <= src < self.__N
      self.__lv = lv = [None]*self.__N; lv[src] = 0
      self.__dist = dist = [inf]*self.__N; dist[src] = 0
      self.__parent = par = [None]*self.__N; par[src] = src
      q = deque([src])
      while q:
        u = q.popleft()
        for v, e in self.__edges[u].items():
          if e.capacity == 0 or lv[v] is not None: continue
          lv[v] = lv[u] + 1
          dist[v] = dist[u] + e.weight
          par[v] = u
          q.append(v)
      
      if tree: self.__depth = lv
      return lv # depth in tree, or level in general graph.

    def dinic(self, src, sink):
      def flow_to_sink(u, flow_in):
        if u == sink: return flow_in
        flow = 0
        for v, e in self.__edges[u].items():
          if e.capacity == 0 or self.__lv[v] <= self.__lv[u]: continue 
          f = flow_to_sink(v, min(flow_in, e.capacity))
          if not f: continue
          self.__edges[u][v].capacity -= f
          if u in self.__edges[v]: self.__edges[v][u].capacity += f
          else: self.add_edge(v, u, capacity=f)
          flow_in -= f
          flow += f
        return flow

      flow = 0
      while True:
        self.bfs(src)
        if self.__lv[sink] is None: return flow
        flow += flow_to_sink(src, inf)
      
    def ford_fulkerson(self):
      pass

    def push_relabel(self):
      pass

    def floyd_warshall(self):
      n = self.__N
      d = [[inf]*n for _ in range(n)]
      for u in range(n):
        d[u][u] = 0
        for v, e in self.__edges[u].items(): d[u][v] = e.weight
      for w in range(n):
        for u in range(n):
          for v in range(n):
            d[u][v] = min(d[u][v], d[u][w]+d[w][v])
      return d
    
    def dijkstra(self, src, paths_cnt=False, mod=None):
      dist = [inf] * self.__N; dist[src] = 0
      visited = [False] * self.__N
      paths = [0] * self.__N; paths[src] = 1
      q = [(0, src)]
      while q:
        d, u = heappop(q)
        if visited[u]: continue
        visited[u] = True
        for v, e in self.__edges[u].items():
          dv = d + e.weight
          if dv > dist[v]: continue
          elif dv == dist[v]:
            paths[v] += paths[u]
            if mod: paths[v] %= mod
            continue 
          paths[v] = paths[u]
          dist[v] = dv
          heappush(q, (dv, v))
      if paths_cnt: return dist, paths 
      else: return dist

    def astar(self, src, tgt, heuristic_func):
      cost = [inf] * self.__N
      q = [(heuristic_func(src, tgt), 0, src)]
      while q:
        _, c, u = heappop(q)
        if u == tgt: return c
        if cost[u] != inf: continue 
        cost[u] = c
        for v, e in self.__edges[u].items():
          if cost[v] != inf: continue
          h = heuristic_func(v, tgt)
          nc = c + e.weight
          heappush(q, (h+nc, nc, v))        
      return inf
    
    
    def find_ancestors(self): # tree doubling.
      self.__ancestors = ancestors = [self.__parent]
      for _ in range(max(self.__depth).bit_length()):
        ancestors.append([ancestors[-1][u] for u in ancestors[-1]])


    def find_dist(self, u, v):
      return self.__dist[u]+self.__dist[v]-2*self.__dist[self.__find_lca(u, v)]

    
    def __find_lca(self, u, v):
      du, dv = self.__depth[u], self.__depth[v]
      if du > dv:
        u, v = v, u 
        du, dv = dv, du 
      
      d = dv - du
      for i in range(d.bit_length()): # up-stream
        if d>>i&1: v = self.__ancestors[i][v]
      if v == u: return v

      for i in range(du.bit_length()-1, -1, -1): # find direct child of LCA.
        nu, nv = self.__ancestors[i][u], self.__ancestors[i][v]
        if nu == nv: continue 
        u, v = nu, nv 
      
      return self.__ancestors[0][u]


  @staticmethod
  def triangle_area(p0, p1, p2, signed=False):
    x1, y1, x2, y2 = p1[0]-p0[0], p1[1]-p0[1], p2[0]-p0[0], p2[1]-p0[1]
    return (x1*y2 - x2*y1)/2 if signed else abs(x1*y2 - x2*y1)/2 
  
  @classmethod
  def intersect(cls, seg1, seg2):
    (p1, p2), (p3, p4) = seg1, seg2
    t1 = cls.triangle_area(p1, p2, p3, signed=True)
    t2 = cls.triangle_area(p1, p2, p4, signed=True)
    t3 = cls.triangle_area(p3, p4, p1, signed=True)
    t4 = cls.triangle_area(p3, p4, p2, signed=True)
    return (t1*t2<0) & (t3*t4<0)
  
  class UnionFind:
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

def cumxor(a): return reduce(xor, a, 0)
def cumor(a): return reduce(or_, a, 0)

def bit_count(n):
  cnt = 0
  while n:
    cnt += n&1
    n >>= 1 
  return cnt


class AtCoder:
  class ABC001:
    @staticmethod
    def a():
      h1, h2 = map(int, sys.stdin.read().split()); print(h1-h2)
    
    @staticmethod 
    def d():
      def to_minuites(x):
        q, r = divmod(x, 100)
        return 60*q + r

      def to_hmform(x):
        q, r = divmod(x, 60)
        return 100*q + r

      n = int(sys.stdin.readline().rstrip())
      term = [0] * 2001
      for _ in range(n):
        s, e = map(to_minuites, map(int, sys.stdin.readline().rstrip().split('-')))
        s = s//5 * 5 
        e = (e+4)//5 * 5
        term[s] += 1
        term[e+1] -= 1
      for i in range(2000):
        term[i+1] += term[i]
      
      res = []
      raining = False
      for i in range(2001):
        if term[i]:
          if not raining: 
            s = i
            raining = True
        elif raining:
          res.append((s, i-1))
          raining = False
      for s, e in res:
        print(f'{to_hmform(s):04}-{to_hmform(e):04}')
          
      

      
  class ABC002:
    @staticmethod
    def a():
      print(max(map(int, sys.stdin.readline().split())))

    @staticmethod 
    def b():
      vowels = set('aeiou')
      print(''.join([c for c in sys.stdin.readline().rstrip() if c not in vowels]))
    
    @staticmethod 
    def c():
      print(GeometryTopology.triangle_area(*map(int, sys.stdin.readline().split())))

    @staticmethod 
    def d():
      n, m = map(int, sys.stdin.readline().split())
      edges = set((x-1, y-1) for x, y in zip(*[map(int, sys.stdin.read().split())]*2))
      print(max(len(s) for i in range(1, 1<<n) for s in [[j for j in range(n) if i>>j&1]] if all((x, y) in edges for x, y in itertools.combinations(s, 2))))

    @staticmethod
    def d_2():
      n, m = map(int, sys.stdin.readline().split())
      relations = [1<<i for i in range(n)]
      for x, y in zip(*[map(int, sys.stdin.read().split())]*2):
        x -= 1; y -= 1
        relations[x] |= 1<<y
        relations[y] |= 1<<x
      res = 0
      for i in range(1<<n):
        cnt = 0
        s = 0
        t = (1<<n) - 1
        for j in range(n):
          if i>>j & 1:
            s |= 1<<j
            t &= relations[j]
            cnt += 1
        if t&s == s: res = max(res, cnt)
      print(res)

  class ABC003:
    @staticmethod
    def a():
      print((int(sys.stdin.readline().rstrip())+1)*5000)
    @staticmethod
    def b():
      atcoder = set('atcoder')
      s, t = sys.stdin.read().split()
      print(all(s[i]==t[i] or s[i]=='@' and t[i] in atcoder or t[i]=='@' and s[i] in atcoder for i in range(len(s))) and 'You can win' or 'You will lose')

    @staticmethod
    def c():
      n, k, *r = map(int, sys.stdin.read().split()); print(reduce(lambda x, y: (x+y)/2, sorted(r)[-k:], 0))

  class ABC004:
    @staticmethod
    def a():
      print(int(sys.stdin.readline().rstrip())*2)
    @staticmethod
    def b():
      for l in [sys.stdin.readline().rstrip() for _ in range(4)][::-1]: print(l[::-1])
    @staticmethod
    def c():
      n = int(sys.stdin.readline().rstrip())%30
      res = list(range(1, 7))
      for i in range(n): i %= 5; res[i], res[i+1] = res[i+1], res[i]
      print(*res, sep='')



  class ABC005:
    @staticmethod
    def a():
      x, y = map(int, sys.stdin.readline().split())
      print(y//x)
    @staticmethod
    def b():
      n, *t = map(int, sys.stdin.read().split())
      print(min(t))
    @staticmethod
    def c():
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
    @staticmethod
    def d():
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


  class ABC006:
    @staticmethod
    def a():
      n = sys.stdin.readline().rstrip()
      if '3' in n: print('YES')
      elif int(n)%3 == 0: print('YES')
      else: print('NO')

    @staticmethod
    def b():
      mod = 10007
      a = np.eye(N=3, k=-1, dtype=np.int64); a[0] = 1
      n = int(sys.stdin.readline().rstrip())
      a = Algebra.matrix_pow(a, n-1, mod)
      print(a[2][0])


    @staticmethod
    def c():
      n, m = map(int, sys.stdin.readline().split())
      cnt = [0, 0, 0]
      if m == 1: cnt = [-1, -1, -1]
      else:
        if m & 1: m -= 3; cnt[1] += 1; n -= 1
        cnt[2] = m//2 - n 
        cnt[0] = n - cnt[2]
      if cnt[0]<0 or cnt[1]<0 or cnt[2]<0: print(-1, -1, -1)
      else: print(*cnt, sep=' ')

    @staticmethod
    def d():
      n, *c = map(int, sys.stdin.read().split())
      lis = [inf]*n 
      for x in c: lis[bi_l(lis, x)] = x 
      print(n - bi_l(lis, inf))

  class ABC007:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      print(n-1)
    @staticmethod
    def b():
      s = sys.stdin.readline().rstrip()
      if s == 'a': print(-1)
      else: print('a')
    @staticmethod
    def c():
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
    @staticmethod
    def d():
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
          
  class ABC008:
    @staticmethod
    def a():
      s, t = map(int, sys.stdin.readline().split())
      print(t-s+1)
    @staticmethod
    def b():
      n, *s = sys.stdin.read().split()
      res = defaultdict(int)
      for name in s: res[name] += 1
      print(sorted(res.items(), key=lambda x: x[1])[-1][0])
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      c = n - np.count_nonzero(a[:, None]%a, axis=1)
      print(np.sum((c+1)//2/c))

    @staticmethod 
    def d():
      w, h, n, *xy = map(int, sys.stdin.read().split())
      *xy, = zip(*([iter(xy)]*2))

      @lru_cache(maxsize=None)
      def count(x1, y1, x2, y2):
        res = 0
        for x, y in xy:
          if not (x1 <= x <= x2 and y1 <= y <= y2): continue
          cnt = (x2-x1) + (y2-y1) + 1
          cnt += count(x1, y1, x-1, y-1)
          cnt += count(x1, y+1, x-1, y2)
          cnt += count(x+1, y1, x2, y-1)
          cnt += count(x+1, y+1, x2, y2)
          res = max(res, cnt)
        return res 
      print(count(1, 1, w, h))


  class ABC009:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      print((n+1)//2)
    @staticmethod
    def b():
      n, *a = map(int, sys.stdin.read().split())
      print(sorted(set(a))[-2])
    @staticmethod
    def c():
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
    
    @staticmethod 
    def d():
      k, m = map(int, sys.stdin.readline().split())
      a = np.array([int(x) for x in sys.stdin.readline().split()])
      c = np.array([int(x) for x in sys.stdin.readline().split()])
      mask = (1<<32) - 1
      d = np.eye(k, k, -1, dtype=np.uint32) * mask; d[0] = c 
      if m <= k: print(a[m-1]); return 
      # print(Algebra.bitwise_mat_pow(d, m-k))
      # print(Algebra.bitwise_dot(Algebra.bitwise_mat_pow(d, m-k), a[::-1].reshape(-1, 1))[0].item())
      print(Algebra.bitwise_dot(Algebra.bitwise_mat_pow(d, m-k), a[::-1].reshape(-1, 1))[0][0])

        
        
  class ABC010:
    @staticmethod
    def a():
      print(sys.stdin.readline().rstrip()+'pp')
    @staticmethod
    def b():
      n, *a = map(int, sys.stdin.read().split())
      tot = 0
      for x in a:
        c = 0 
        while x%2==0 or x%3==2:
          x -= 1
          c += 1
        tot += c
      print(tot)
    @staticmethod
    def c():
      sx, sy, gx, gy, t, v, n, *xy = map(int, sys.stdin.read().split())
      x, y = np.array(xy).reshape(-1, 2).T
      def dist(x1, y1, x2, y2):
        return np.sqrt((x2-x1)**2 + (y2-y1)**2)
      ans = 'YES' if (dist(sx, sy, x, y)+dist(x, y, gx, gy) <= v*t).any() else 'NO'
      print(ans)
    
    @staticmethod
    def d():
      n, g, e = map(int, sys.stdin.readline().split())
      p = [int(x) for x in sys.stdin.readline().split()]
      x, y = [], []
      for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        x.append(a); y.append(b)
        x.append(b); y.append(a)
      for a in p:
        x.append(a)
        y.append(n)
      if not x:
        print(0)
        return
      c = [1] * len(x)
      min_cut = maximum_flow(csr_matrix((c, (x, y)), (n+1, n+1)), source=0, sink=n).flow_value
      print(min_cut)
    
    @staticmethod
    def d_2():
      n, g, e = map(int, sys.stdin.readline().split())
      graph = nx.DiGraph() 
      graph.add_nodes_from(range(n+1))
      for p in [int(x) for x in sys.stdin.readline().split()]:
        graph.add_edge(p, n, capacity=1)
      for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph.add_edge(a, b, capacity=1)
        graph.add_edge(b, a, capacity=1)
      print(nx.minimum_cut_value(graph, 0, n))

    @staticmethod
    def d_3():
      n, q, m = map(int, sys.stdin.readline().split())
      g = GeometryTopology.Graph(n+1)
      # for i in range(n+1): g.add_node(i)
      for p in [int(x) for x in sys.stdin.readline().split()]:
        g.add_edge(p, n, capacity=1)
      for a, b in zip(*[map(int, sys.stdin.read().split())]*2):
        g.add_edge(a, b, capacity=1)
        g.add_edge(b, a, capacity=1)
      print(g.dinic(0, n))



  class ABC011:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      print(n%12+1)
    @staticmethod
    def b():
      s = sys.stdin.readline().rstrip() 
      print(s[0].upper()+s[1:].lower())
    @staticmethod
    def c():
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
      
    @staticmethod 
    def d():
      n, d, x, y = map(int, sys.stdin.read().split())
      x, y = abs(x), abs(y)
      if x%d or y%d: print(0); return 
      x, y = x//d, y//d
      r = n - (x+y)
      if r < 0 or r&1: print(0); return

      res = 0
      half_p = pow(1/2, n)
      for d in range(r//2 + 1): # 0 <= d <= r//2, south 
        south, north = d, y+d  
        west = (r - 2*d)//2
        res += half_p * comb(n, south, exact=True) * comb(n-south, north, exact=True)\
                      * comb(n-south-north, west, exact=True) * half_p
      print(res)

  
  class ABC012:
    @staticmethod
    def a():
      a, b = map(int, sys.stdin.readline().split())
      print(b, a)
    
    @staticmethod 
    def b():
      n = int(sys.stdin.readline().rstrip())
      h, n = divmod(n, 3600)
      m, s = divmod(n, 60)
      print(f'{h:02}:{m:02}:{s:02}')
    
    @staticmethod
    def c():
      n = 2025 - int(sys.stdin.readline().rstrip())
      res = []
      for i in range(1, 10):
        if n%i != 0 or n//i > 9: continue 
        res.append(f'{i} x {n//i}')
      print(*sorted(res), sep='\n')

    @staticmethod
    def d():
      n, m, *abt = map(int, sys.stdin.read().split())
      a, b, t = np.array(abt).reshape(m, 3).T 
      res = shortest_path(csr_matrix((t, (a-1, b-1)), (n, n)), method='FW', directed=False)
      print(res.max(axis=-1).min().astype(np.int64))
    
    @staticmethod
    def d_2():
      n, m, *abt = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph(n)
      for a, b, t in zip(*[iter(abt)]*3):
        a -= 1; b -= 1
        g.add_edge(a, b, weight=t)
        g.add_edge(b, a, weight=t)
      
      print(min(max(d) for d in g.floyd_warshall()))



  class ABC013:
    @staticmethod 
    def a():
      print(ord(sys.stdin.readline().rstrip()) - ord('A') + 1)

    @staticmethod 
    def b():
      a, b = map(int, sys.stdin.read().split())
      d = abs(a - b)
      print(min(d, 10-d))

    @staticmethod 
    def c():
      n, h, a, b, c, d, e = map(int, sys.stdin.read().split())
      y = np.arange(n+1)
      x = (n*e-h-(d+e)*y)//(b+e) + 1
      np.maximum(x, 0, out=x)
      np.minimum(x, n-y, out=x)
      print(np.amin(a*x + c*y))

    @staticmethod 
    def d():
      n, m, d, *a = map(int, sys.stdin.read().split())
      res = list(range(n))
      
      def swap(i, j): res[i], res[j] = res[j], res[i]
      for i in a[::-1]: swap(i-1, i)

      group = [None] * n 
      root = [None] * n
      index_in_group = [None] * n
      for i in range(n):
        if root[i] is not None: continue
        group[i] = []
        j = i 
        for cnt in range(1, n+1):
          index_in_group[j] = cnt-1
          group[i].append(j)
          j = res[j]
          root[j] = i
          if j == i: break
      
      for i in range(n):
        g = group[root[i]]
        print(g[(index_in_group[i]+d)%len(g)] + 1)

  class ABC014:
    @staticmethod 
    def a():
      a, b = map(int, sys.stdin.read().split())
      print((a+b-1)//b * b - a)
    
    @staticmethod
    def b():
      n, x, *a = map(int, sys.stdin.read().split())
      print(sum(a[i] for i in range(n) if x>>i&1))

    @staticmethod
    def c():
      n, *ab = map(int, sys.stdin.read().split())
      a, b = np.array(ab).reshape(n, 2).T 
      res = np.zeros(10**6+2, dtype=np.int64)
      np.add.at(res, a, 1)
      np.subtract.at(res, b+1, 1)
      np.cumsum(res, out=res)
      print(res.max())

    @staticmethod 
    def d():
      n = int(sys.stdin.readline().rstrip())
      g = GeometryTopology.Graph(n)
      for _ in range(n-1):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1; y -= 1
        g.add_edge(x, y, weight=1)
        g.add_edge(y, x, weight=1)
    
      g.bfs(tree=True)
      g.find_ancestors()

      q, *ab = map(int, sys.stdin.read().split())
      for a, b in zip(*[iter(ab)]*2):
        a -= 1; b -= 1
        print(g.find_dist(a, b) + 1)
  
  class ABC015:
    @staticmethod 
    def a():
      a, b = sys.stdin.read().split()
      print(a if len(a) > len(b) else b)

    @staticmethod 
    def b():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      print(np.ceil(a[np.nonzero(a)[0]].sum() / np.count_nonzero(a)).astype(np.int8))
    
    @staticmethod 
    def c():
      n, k, *t = map(int, sys.stdin.read().split())
      t = np.array(t).reshape(n, k)
      x = np.zeros((1, 1), dtype=np.int8)
      for i in range(n):
        x = x.reshape(-1, 1) ^ t[i]
      print('Found' if np.count_nonzero(x==0) > 0 else 'Nothing')
    
    @staticmethod 
    def d():
      w, n, k, *ab = map(int, sys.stdin.read().split())
      dp = np.zeros((k+1, w+1), dtype=np.int32)
      for a, b in zip(*[iter(ab)]*2):
        prev = dp.copy()
        np.maximum(dp[1:, a:], prev[:-1, :-a] + b, out=dp[1:, a:])
      print(dp[k][w])

  
  class ABC016:
    @staticmethod 
    def a():
      m, d = map(int, sys.stdin.readline().split())
      print('YES' if m%d == 0 else 'NO')
    
    @staticmethod 
    def b():
      a, b, c = map(int, sys.stdin.readline().split())
      f1, f2 = a+b==c, a-b==c 
      if f1 & f2: print('?')
      elif f1 & (~f2): print('+')
      elif (~f1) & f2: print('-')
      else: print('!')
    
    @staticmethod 
    def c():
      n, _, *ab = map(int, sys.stdin.read().split())
      friends = [0] * n
      for a, b in zip(*[iter(ab)]*2):
        a -= 1; b -= 1
        friends[a] |= 1<<b
        friends[b] |= 1<<a
      res = [bit_count(cumor(friends[j] for j in range(n) if friends[i]>>j&1) & ~(friends[i] | 1<<i)) for i in range(n)]
      print(*res, sep='\n')
    
    @staticmethod 
    def d():
      sx, sy, gx, gy = map(int, sys.stdin.readline().split())
      seg1 = ((sx, sy), (gx, gy))
      n = int(sys.stdin.readline().rstrip())
      p1 = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, 2).T
      p2 = np.hstack((p1[:, 1:], p1[:, :1]))
      seg2 = (p1, p2)
      print(np.count_nonzero(GeometryTopology.intersect(seg1, seg2))//2 + 1)

  class ABC017:
    @staticmethod 
    def a():
      s, e = np.array(sys.stdin.read().split(), dtype=np.int16).reshape(3, 2).T
      print((s // 10 * e).sum())

    @staticmethod 
    def b():
      choku_tail = set('ch, o, k, u'.split(', '))
      def is_choku(s):
        if s == '': return True 
        if len(s)>=1 and (s[-1] in choku_tail) and is_choku(s[:-1]): return True 
        if len(s)>=2 and (s[-2:] in choku_tail) and is_choku(s[:-2]): return True
        return False 
      print('YES' if is_choku(sys.stdin.readline().rstrip()) else 'NO') 

    @staticmethod 
    def c():
      n, m, *lrs = map(int, sys.stdin.read().split())
      l, r, s = np.array(lrs).reshape(n, 3).T 
      score = np.zeros((m+1, ), dtype=np.int32)
      np.add.at(score, l-1, s)
      np.subtract.at(score, r, s)
      np.cumsum(score, out=score)
      print(s.sum() - score[:m].min())

    @staticmethod 
    def d():
      n, m, *f = map(int, sys.stdin.read().split())
      prev = [0] * (n+1)
      tmp = defaultdict(int)
      for i in range(n):
        prev[i+1] = tmp[f[i]]
        tmp[f[i]] = i+1

      dp = [0] * (n+1); dp[0] = 1
      l, s = 0, dp[0]
      for i in range(1, n+1):
        while l < prev[i]:
          s = (s - dp[l]) % MOD
          l += 1
        dp[i] = s
        s = (s + dp[i]) % MOD
      print(dp[n])
  
  class ABC018:
    @staticmethod 
    def a():
      *a, = map(int, sys.stdin.read().split())
      a = sorted(enumerate(a), key=lambda x: -x[1])
      res = [None] * 3
      for i in range(3):
        res[a[i][0]] = i+1
      print(*res, sep='\n')
    
    @staticmethod 
    def b():
      s = sys.stdin.readline().rstrip()
      n, *lr = map(int, sys.stdin.read().split())
      for l, r in zip(*[iter(lr)]*2):
        l -= 1; r -= 1
        s = s[:l] + s[l:r+1][::-1] + s[r+1:]
      print(s)

    @staticmethod 
    def c():
      r, c, k = map(int, sys.stdin.readline().split())
      s = np.array([list(s) for s in sys.stdin.read().split()])
      s = np.pad(s, 1, constant_values='x')

      a = np.zeros_like(s, dtype=np.float64)
      a[s=='o'] = np.inf
      for i in range(1, r+1): np.minimum(a[i-1,:]+1, a[i,:], out=a[i,:])
      for i in range(r, 0, -1): np.minimum(a[i+1,:]+1, a[i,:], out=a[i,:])
      for j in range(1, c+1): np.minimum(a[:,j-1]+1, a[:,j], out=a[:,j])
      for j in range(c, 0, -1): np.minimum(a[:,j+1]+1, a[:,j], out=a[:,j])
      print(np.count_nonzero(a>=k))
    
    @staticmethod 
    def c_2():
      r, c, k = map(int, sys.stdin.readline().split())
      s = np.array([list(s) for s in sys.stdin.read().split()])
      s = np.pad(s, 1, constant_values='x')
      a = (s=='o').astype(np.int16)
      a = distance_transform_cdt(a, metric='taxicab')
      print(np.count_nonzero(a>=k))
    
    @staticmethod
    def d():
      n, m, p, q, r, *xyz = map(int, sys.stdin.read().split())
      x, y, z = np.array(xyz).reshape(r, 3).T 
      h = np.zeros((n, m), dtype=np.int32); h[x-1, y-1] = z
      g = np.array([*itertools.combinations(range(n), p)])
      print(np.sort(h[g].sum(axis=1), axis=1)[:,-q:].sum(axis=1).max())

    
  class ABC019:
    @staticmethod 
    def a():
      *a, = map(int, sys.stdin.readline().split())
      print(sorted(a)[1])

    @staticmethod 
    def b():
      s = sys.stdin.readline().rstrip() + '$'
      cnt = 0
      prev = '$'
      t = ''
      for c in s:
        if c == prev: cnt += 1; continue
        t += prev+str(cnt)
        prev = c; cnt = 1 
      print(t[2:])
    
    @staticmethod 
    def c():
      n, *a = map(int, sys.stdin.read().split())
      res = set()
      for x in a:
        while not x&1:
          x >>= 1
        res.add(x)
      print(len(res))
    
    @staticmethod 
    def d():
      def inquire(u, v):
        print(f'? {u} {v}'.format(u, v), flush=True)
        return int(sys.stdin.readline().rstrip())
      
      n = int(sys.stdin.readline().rstrip())
      u = sorted([(inquire(1, v), v) for v in range(2, n+1)])[-1][1]
      d = max((inquire(u, v)) for v in range(1, n+1) if u!=v)
      print(f'! {d}')
    
  class ABC020:
    @staticmethod 
    def a():
      print('ABC' if int(sys.stdin.readline().rstrip())==1 else 'chokudai')
    
    @staticmethod 
    def b():
      a, b = sys.stdin.readline().split()
      print(int(a+b) * 2)
    
    @staticmethod 
    def c():
      h, w, t = map(int, sys.stdin.readline().split())
      s = [list(s) for s in sys.stdin.read().split()]
      for i in range(h):
        for j in range(w):
          if s[i][j] == 'S': sy, sx = i, j 
          if s[i][j] == 'G': gy, gx = i, j
      s[sy][sx] = s[gy][gx] = '.'
      source, target = (sy,sx), (gy,gx)
      

      def heuristic_function(u, v=target):
        return abs(v[0]-u[0]) + abs(v[1]-u[0])

      def min_time(x):
        '''my lib'''
        graph = GeometryTopology.Graph()
        for i in range(h):
          for j in range(w):
            graph.add_node((i,j))
        for i in range(h):
          for j in range(w):
            if i > 0: graph.add_edge((i,j), (i-1,j), weight=(1 if s[i-1][j]=='.' else x))
            if i < h-1: graph.add_edge((i,j), (i+1,j), weight=(1 if s[i+1][j]=='.' else x))
            if j > 0: graph.add_edge((i,j), (i,j-1), weight=(1 if s[i][j-1]=='.' else x))
            if j < w-1: graph.add_edge((i,j), (i,j+1), weight=(1 if s[i][j+1]=='.' else x))

        return graph.dijkstra(source)[target]
        # return graph.astar(source, target, heuristic_function)

        '''networkx'''
        graph = nx.DiGraph()

        for i in range(h):
          for j in range(w):
            if i > 0: graph.add_edge((i,j), (i-1,j), weight=(1 if s[i-1][j]=='.' else x))
            if i < h-1: graph.add_edge((i,j), (i+1,j), weight=(1 if s[i+1][j]=='.' else x))
            if j > 0: graph.add_edge((i,j), (i,j-1), weight=(1 if s[i][j-1]=='.' else x))
            if j < w-1: graph.add_edge((i,j), (i,j+1), weight=(1 if s[i][j+1]=='.' else x))

        return nx.dijkstra_path_length(graph, source, target)
        return nx.astar_path_length(graph, source, target, heuristic_function)

      def binary_search():
        lo, hi = 1, t+1
        while lo+1 < hi:
          x = (lo+hi)//2
          if min_time(x) > t:
            hi = x 
          else:
            lo = x
        return lo

      print(binary_search())
            
    @staticmethod 
    def d():
      n, k = map(int, sys.stdin.readline().split())
      div = sorted(NumberTheory.find_divisors(k))
      l = len(div)
      s = [0] * l
      for i, d in enumerate(div): s[i] = (1+n//d)*(n//d)//2 * d % MOD
      for i in range(l-1, -1, -1):
        for j in range(i+1, l):
          if div[j]%div[i]: continue 
          s[i] = (s[i]-s[j])%MOD
      
      print(sum(s[i]*k//div[i]%MOD for i in range(l))%MOD) # ans is LCM.

  class ABC021:
    @staticmethod 
    def a():
      n  = int(sys.stdin.readline().rstrip())
      s = [1<<i for i in range(5) if n>>i&1]
      print(len(s), *s, sep='\n')
    
    @staticmethod 
    def b():
      n, a, b, k, *p = map(int, sys.stdin.read().split())
      print('YES' if len(set(p)|set([a, b])) == k+2 else 'NO')

    @staticmethod 
    def c():
      n, a, b, m, *xy = map(int, sys.stdin.read().split())
      x, y = np.array(xy).reshape(m, 2).T - 1
      a -= 1; b -= 1
      g = csgraph_to_dense(csr_matrix((np.ones(m), (x, y)), (n, n), dtype=np.int8))
      g = np.logical_or(g, g.T)
      paths = np.zeros(n, dtype=np.int64).reshape(-1, 1)
      paths[a, 0] = 1 
      while not paths[b, 0]:
        paths = np.dot(g, paths) % MOD
      print(paths[b, 0])

    @staticmethod 
    def c_2():
      n, a, b, m, *xy = map(int, sys.stdin.read().split())
      a -= 1; b -= 1
      g = GeometryTopology.Graph()

      for x, y in zip(*[iter(xy)]*2):
        x -= 1; y -= 1
        g.add_edge(x, y, weight=1)
        g.add_edge(y, x, weight=1)

      dist, paths = g.dijkstra(a, paths_cnt=True, mod=MOD)
      print(paths[b])

    @staticmethod
    def d():
      n, k = map(int, sys.stdin.read().split())
      combinatorics = Combinatorics()
      print(combinatorics.mod_choose(n+k-1, k))

  
  class ABC022:
    @staticmethod 
    def a():
      n, s, t, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      np.cumsum(a, out=a)
      print(((s<=a) & (a<=t)).sum())

    @staticmethod 
    def b():
      n, *a = map(int, sys.stdin.read().split())
      c = Counter(a)
      print(sum(c.values())-len(c))

    @staticmethod
    def c():
      n, m, *uvl = map(int, sys.stdin.read().split())
      u, v, l = np.array(uvl).reshape(m, 3).T
      u -= 1; v -= 1 
      g = csgraph_to_dense(csr_matrix((l, (u,v)), (n,n)))
      g += g.T
      g[g==0] = np.inf
      dist0 = g[0].copy()
      g[0] = 0; g[:, 0] = 0
      dist = shortest_path(g, method='FW', directed=False)
      u, v = np.array([*itertools.combinations(range(1,n), 2)]).T 
      res = (dist0[u]+dist[u,v]+dist0[v]).min()
      print(-1 if res==np.inf else int(res))
    
    @staticmethod 
    def d():
      n, *ab = map(int, sys.stdin.read().split())
      c = np.array(ab).reshape(2,n,2)
      g = c.mean(axis=1)
      d = np.sqrt(((c-g[:,None,:])**2).sum(axis=-1)).sum(axis=1)
      print(d[1]/d[0])


  class ABC023:
    @staticmethod 
    def a():
      print(sum(divmod(int(sys.stdin.readline().rstrip()), 10)))

    @staticmethod 
    def b():
      n, s = sys.stdin.read().split()
      n = int(n)
      t = 'b'
      for i in range(n//2):
        if i%3==0: t = 'a'+t+'c'
        elif i%3==1: t = 'c'+t+'a'
        else: t = 'b'+t+'b'
      print(n//2 if t==s else -1)
    
    @staticmethod 
    def b_2():
      n, s = sys.stdin.read().split() 
      n = int(n)
      if n&1^1: print(-1); return 
      a = list('abc')
      i = (1-n//2)%3
      for c in s:
        if c != a[i]:
          print(-1); return 
        i = (i+1) % 3
      print(n//2)

    @staticmethod 
    def c():
      h, w, k, n, *rc = map(int, sys.stdin.read().split())
      r, c = np.array(rc).reshape(n,2).T - 1
      rb = np.bincount(r, minlength=h)
      cb = np.bincount(c, minlength=w)
      rbb = np.bincount(rb, minlength=k+1)
      cbb = np.bincount(cb, minlength=k+1)
      tot = (rbb[:k+1]*cbb[k::-1]).sum()
      real = np.bincount(rb[r]+cb[c]-1, minlength=k+1)
      print(tot-real[k-1]+real[k])

    @staticmethod 
    def d():
      n, *hs = map(int, sys.stdin.read().split())
      h, s = np.array(hs).reshape(n,2).T
      
      t = np.arange(n)
      def is_ok(x):
        t_lim = (x-h)//s 
        t_lim.sort()
        return np.all(t_lim >= t)

      def binary_search():
        lo, hi = 0, 10**14
        while lo+1 < hi:
          x = (lo+hi)//2
          if is_ok(x):
            hi = x 
          else:
            lo = x 
        return hi
      print(binary_search())

  class ABC024:
    @staticmethod 
    def a():
      a, b, c, k, s, t = map(int, sys.stdin.read().split())
      print(a*s + b*t - c*(s+t)*(s+t>=k)) 

    @staticmethod 
    def b():
      n, t, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      print(np.minimum(a[1:]-a[:-1], t).sum() + t)

    @staticmethod 
    def c():
      n, d, k, *lrst = map(int, sys.stdin.read().split())
      lrst = np.array(lrst)
      lr = lrst[:2*d].reshape(d,2) 
      s, t = lrst[2*d:].reshape(k,2).T
      day = np.zeros((k,),dtype=np.int32)
      for i in range(d):
        l, r = lr[i]
        move = (l<=s)&(s<=r)&(s!=t)
        reach = move&(l<=t)&(t<=r)
        s[move&(s<t)] = r 
        s[move&(s>t)] = l
        s[reach] = t[reach]; day[reach] = i+1
      print(*day, sep='\n')

    @staticmethod 
    def d():
      a, b, c = map(int, sys.stdin.read().split())
      p = MOD
      denom = pow(a*b%p - b*c%p + c*a%p, p-2, p)
      w = (b*c-a*b)%p*denom%p
      h = (b*c-a*c)%p*denom%p
      print(h,w) 

  class ABC025:
    @staticmethod 
    def a():
      s, n = sys.stdin.read().split()
      n = int(n)
      i, j = divmod(n-1, 5)
      print(s[i]+s[j])

    @staticmethod 
    def b():
      n, a, b = map(int, sys.stdin.readline().split())
      res = defaultdict(int)
      for _ in range(n):
        s, d = sys.stdin.readline().split()
        d = int(d)
        res[s] += min(max(d,a),b)
      res = res['East'] - res['West']
      if res == 0: ans = 0 
      elif res > 0: ans = f'East {res}'
      else: ans = f'West {-res}'
      print(ans)

    @staticmethod 
    def c():
      b = [0] * 6
      for i in range(2):
        *row, = map(int, sys.stdin.readline().split())
        for j in range(3):
          b[i*3+j] = row[j]
      c = [0] * 8
      for i in range(3):
        *row, = map(int, sys.stdin.readline().split())
        for j in range(2):
          c[i*3+j] = row[j]
      tot = sum(b) + sum(c) 

      @lru_cache(maxsize=None)
      def f(s=tuple(0 for _ in range(9))):
        if all(s):
          res = 0
          for i in range(6): res += (s[i]==s[i+3])*b[i]
          for i in range(8): res += (s[i]==s[i+1])*c[i]
          return res
        cand = [i for i in range(9) if not s[i]]
        flg = len(cand)&1
        s = list(s)
        res = []
        for i in cand:
          s[i] = (flg^1)+1
          res.append(f(tuple(s)))
          s[i] = 0
        return sorted(res, reverse=flg)[0]

      a = f(); b = tot-a
      print(a)
      print(b)

      

  class ABC026:
    @staticmethod 
    def a():
      a = int(sys.stdin.readline().rstrip())
      print(a//2 * (a-a//2))

    @staticmethod 
    def b():
      n, *r = map(int, sys.stdin.read().split())
      s = np.pi * np.array([0]+r)**2; s.sort()
      res = s[n::-2].sum() - s[n-1::-2].sum()
      print(res)     

    @staticmethod 
    def c():
      n, *b = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph()
      for i in range(1, n): g.add_edge(b[i-1]-1, i, weight=1)

      def f(u=0):
        if not g.edges[u]: return 1 
        s = [f(v) for v in g.edges[u]]
        return max(s) + min(s) + 1

      print(f())

    @staticmethod 
    def d():
      a, b, c = map(int, sys.stdin.readline().split())
      def f(t): return a*t + b*np.sin(c*t*np.pi) - 100
      print(optimize.brenth(f, 0, 200))

  
  class ABC027:
    @staticmethod 
    def a():
      l = [int(l) for l in sys.stdin.readline().split()]
      l.sort()
      print(l[2] if l[0]==l[1] else l[0])

    @staticmethod 
    def b():
      n, *a = map(int, sys.stdin.read().split())
      m, r = divmod(sum(a), n)
      if r: print(-1); return 
      population = 0 
      towns = 0
      cnt = 0
      for x in a:
        population += x 
        towns += 1 
        if population/towns != m: cnt+=1; continue 
        population, towns = 0, 0
      print(cnt)

    @staticmethod 
    def c():
      n = int(sys.stdin.readline().rstrip())
      flg = n.bit_length()&1^1
      t = 0
      x = 1
      while x <= n:
        t += 1
        x = 2*x+1 if t&1^flg else 2*x
      print('Aoki' if t&1 else 'Takahashi')
        



  class ABC032:
    @staticmethod
    def a():
      a, b, n = map(int, sys.stdin.read().split())
      l = NumberTheory.lcm(a, b)
      print((n+l-1)//l*l)

    @staticmethod
    def b():
      s, k = sys.stdin.read().split()
      k = int(k)
      res = set()
      for i in range(len(s)-k+1):
        res.add(s[i:i+k])
      print(len(res))

    @staticmethod
    def c():
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

  class ABC033:
    @staticmethod
    def a():
      n = set(sys.stdin.readline().rstrip())
      print('SAME' if len(n)==1 else 'DIFFERENT')
    @staticmethod
    def b():
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
    @staticmethod
    def c():
      s = sys.stdin.readline().rstrip()
      res = sum(not '0' in f for f in s.split('+'))
      print(res)

  class ABC034:
    @staticmethod
    def a():
      x, y = map(int, sys.stdin.readline().split())
      print('Better' if y>x else 'Worse')
    @staticmethod
    def b():
      n = int(sys.stdin.readline().rstrip())
      print(n+1 if n&1 else n-1)
    @staticmethod
    def c():
      h, w = map(int, sys.stdin.read().split())
      combinatorics = Combinatorics(n=2*10**5, mod=MOD)
      print(combinatorics.mod_choose(h+w-2, h-1))
    @staticmethod
    def d():
      n, k, *wp = map(int, sys.stdin.read().split())
      w, p = np.array(wp).reshape(-1, 2).T 
      def f(x):
        return np.sort(w*(p-x))[-k:].sum()
      print(optimize.bisect(f, 0, 100))

  class ABC035:
    @staticmethod
    def a():
      w, h = map(int, sys.stdin.readline().split())
      print('4:3' if 4*h==3*w else '16:9')
    @staticmethod
    def b():
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

    @staticmethod
    def c():
      n, q, *lr = map(int, sys.stdin.read().split())
      l, r = np.array(lr).reshape(q, 2).T
      res = np.zeros(n+1, dtype=int)
      np.add.at(res, l-1, 1)
      np.subtract.at(res, r, 1)
      np.cumsum(res, out=res)
      res = res&1
      print(''.join(map(str, res[:-1])))

    @staticmethod
    def d():
      n, m, t = map(int, sys.stdin.readline().split())
      point = np.array(sys.stdin.readline().split(), dtype=int)
      a, b, c = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(m, 3).T 
      a -= 1; b -= 1 
      d_1 = shortest_path(csr_matrix((c, (a, b)), (n, n)), method='D', directed=True, indices=0)
      d_2 = shortest_path(csr_matrix((c, (b, a)), (n, n)), method='D', directed=True, indices=0)
      print(int(np.amax((t-(d_1+d_2))*point)))

  class ABC036:
    @staticmethod
    def a():
      a, b = map(int, sys.stdin.readline().split())
      print((b+a-1)//a)

    @staticmethod
    def b():
      n, *s = sys.stdin.read().split()
      n = int(n)
      for j in range(n):
        row = ''
        for i in range(n-1, -1, -1):
          row += s[i][j]
        print(row)
    
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      b = [None]*n
      prev = None
      j = -1
      for i, x in sorted(enumerate(a), key=lambda x: x[1]):
        if x != prev: j += 1
        b[i] = j
        prev = x     
      print(*b, sep='\n') 
    
    @staticmethod
    def d():
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

  class ABC037:
    @staticmethod
    def a():
      a, b, c = map(int, sys.stdin.readline().split())
      print(c//min(a, b))

    @staticmethod
    def b():
      n, q, *lrt = map(int, sys.stdin.read().split())
      a = np.zeros(n, dtype=int)
      for l, r, t in zip(*[iter(lrt)]*3):
        a[l-1:r] = t 
      print(*a, sep='\n')
    
    @staticmethod
    def c():
      n, k, *a = map(int, sys.stdin.read().split())
      a = np.array([0]+a)
      np.cumsum(a, out=a)
      s = (a[k:] - a[:-k]).sum()
      print(s)
    
    @staticmethod
    def d():
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

  class ABC038:
    @staticmethod
    def a():
      s = sys.stdin.readline().rstrip()
      print('YES' if s[-1]=='T' else 'NO')
    
    @staticmethod
    def b():
      a, b, c, d = map(int, sys.stdin.read().split())
      print('YES' if a==c or b==c or a==d or b==d else 'NO')
    
    @staticmethod
    def c():
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
    
    @staticmethod
    def d():
      n, *wh = map(int, sys.stdin.read().split())
      wh = sorted(zip(*[iter(wh)]*2), key=lambda x: (-x[0], x[1]))
      w = [x[1] for x in wh][::-1]
      res = [inf] * n 
      for x in w:
        res[bi_l(res, x)] = x
      print(bi_l(res, inf))

  class ABC039:
    @staticmethod
    def a():
      a, b, c = map(int, sys.stdin.readline().split())
      print((a*b+b*c+c*a)*2)
    
    @staticmethod
    def b():
      x = int(sys.stdin.readline().rstrip())
      for n in range(1, int(x**0.5)+1):
        if pow(n, 4)==x:
          print(n); return

    
    @staticmethod
    def c():
      board = 'WBWBWWBWBWBW' * 3
      convert = 'Do, *, Re, *, Mi, Fa, *, So, *, La, *, Si'.split(', ')
      s = sys.stdin.readline().rstrip()
      print(convert[board.index(s)])

    @staticmethod
    def d():
      h, w = map(int, sys.stdin.readline().split())
      s = sys.stdin.read().split()
      dyx = list(itertools.product((-1, 0, 1), repeat=2))
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
            
  class ABC040:
    @staticmethod
    def a():
      n, x = map(int, sys.stdin.readline().split())
      print(min(x-1, n-x))

    @staticmethod
    def b():
      n = int(sys.stdin.readline().rstrip())
      res = inf 
      for i in range(1, int(n**.5)+1):
        res = min(res, n//i-i+n%i)
      print(res)

    @staticmethod
    def c():
      n, *h = map(int, sys.stdin.read().split())
      h = [h[0]]+h
      cost = [None] * (n+1); cost[0] = cost[1] = 0
      for i in range(2, n+1):
        cost[i] = min(
          cost[i-2] + abs(h[i]-h[i-2]),
          cost[i-1] + abs(h[i]-h[i-1])
        )
      print(cost[n])

    @staticmethod
    def d():
      n, m = map(int, sys.stdin.readline().split())
      uf = GeometryTopology.UnionFind(n=n)
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

  class ABC041:
    @staticmethod
    def a():
      s, i = sys.stdin.read().split()
      i = int(i)
      print(s[i-1])
    
    @staticmethod
    def b():
      a, b, c = map(int, sys.stdin.readline().split())
      ans = a * b % MOD * c % MOD 
      print(ans)
    
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      for i, h in sorted(enumerate(a), key=lambda x: -x[1]):
        print(i+1)
    
    @staticmethod
    def d():
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

  class ABC042:
    @staticmethod
    def a():
      a = [int(x) for x in sys.stdin.readline().split()]
      c = Counter(a)
      print('YES' if c[5]==2 and c[7]==1 else 'NO')
    
    @staticmethod
    def b():
      n, l, *s = sys.stdin.read().split()
      print(''.join(sorted(s)))

    @staticmethod
    def c():
      n, k, *d = sys.stdin.read().split()
      l = len(n)
      ok = sorted(set(string.digits)-set(d))
      cand = [int(''.join(p)) for p in itertools.product(ok, repeat=l)] + [int(min(x for x in ok if x > '0')+min(ok)*l)]
      print(cand[bi_l(cand, int(n))])
    
    @staticmethod
    def d():
      h, w, a, b = map(int, sys.stdin.read().split())
      combinatorics = Combinatorics(n=2*10**5, mod=MOD)
      tot = combinatorics.mod_choose(h+w-2, h-1)
      i = np.arange(h-a, h)
      ng = np.sum(combinatorics.mod_choose(i+b-1, i) * combinatorics.mod_choose(h-i+w-b-2, h-1-i) % MOD)
      tot -= ng; tot %= MOD
      print(tot)

  class ABC043:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      print((1+n)*n//2)
    
    @staticmethod
    def b():
      s = sys.stdin.readline().rstrip()
      t = ''
      for c in s:
        if c == 'B': t = t[:-1]
        else: t += c
      print(t)
    
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      x = np.around(a.sum()/n).astype(int)
      print(np.sum((a-x)**2))
    
    @staticmethod
    def d():
      s = sys.stdin.readline().rstrip()
      n = len(s)
      for i in range(n-1):
        if s[i] == s[i+1]:
          print(i+1, i+2); return 
      for i in range(n-2):
        if s[i] == s[i+2]:
          print(i+1, i+3); return 
      print(-1, -1)

  class ABC170:
    @staticmethod
    def a():
      x = [int(x) for x in sys.stdin.readline().split()]
      for i in range(5):
        if x[i] != i+1:
          print(i+1)
          break
    
    @staticmethod
    def b():
      x, y = map(int, sys.stdin.readline().split())
      print('Yes' if 2*x <= y <= 4*x and y%2 == 0 else 'No')
    @staticmethod
    def c():
      x, n, *p = map(int, sys.stdin.read().split())
      a = list(set(range(102)) - set(p))
      a = [(abs(y-x), y) for y in a]
      print(sorted(a)[0][1])
    
    @staticmethod
    def d():
      n, *a = map(int, sys.stdin.read().split())
      cand = set(a)
      cnt = 0
      for x, c in sorted(Counter(a).items()):
        cnt += c == 1 and x in cand
        cand -= set(range(x*2, 10**6+1, x))
      print(cnt)

    @staticmethod
    def e():
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
      


  class ABC171:
    @staticmethod
    def a():
      c = sys.stdin.readline().rstrip()
      print('A' if c < 'a' else 'a')
    
    @staticmethod
    def b():
      n, k, *p = map(int, sys.stdin.read().split())
      print(sum(sorted(p)[:k]))
    

    @staticmethod
    def c():
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
    
    @staticmethod
    def d():
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
    
    @staticmethod
    def e():
      n, *a = map(int, sys.stdin.read().split())
      s = 0
      for x in a: s ^= x 
      b = map(lambda x: x^s, a)
      print(*b, sep=' ')


  class ABC172:
    @staticmethod
    def a():
      a = int(sys.stdin.readline().rstrip()); print(a*(1+a+a**2))
    
    @staticmethod
    def b():
      s, t = sys.stdin.read().split(); print(sum(s[i]!=t[i] for i in range(len(s))))
    
    @staticmethod
    def c():
      n, m, k = map(int, sys.stdin.readline().split())
      a = [0] + [int(x) for x in sys.stdin.readline().split()]
      b = [int(x) for x in sys.stdin.readline().split()]
      *sa, = itertools.accumulate(a)
      *sb, = itertools.accumulate(b)
      res = 0
      for i in range(n+1):
        r = k - sa[i]
        if r < 0: break 
        res = max(res, i+bi_r(sb, r))
      print(res)

    @staticmethod 
    def d():
      n = int(sys.stdin.readline().rstrip())
      f = np.zeros(n+1, dtype=np.int64)
      for i in range(1, n+1):
        f[i::i] += 1
      print((np.arange(1, n+1)*f[1:]).sum())


  class ABC173:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      charge = (n+999)//1000 * 1000 - n
      print(charge)
    
    @staticmethod
    def b():
      n, *s = sys.stdin.read().split() 
      c = Counter(s)
      for v in 'AC, WA, TLE, RE'.split(', '):
        print(f'{v} x {c[v]}')
    

    @staticmethod
    def c():
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

    @staticmethod
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a.sort(reverse=True)
      res = a[0] + sum(a[1:1+(n-2)//2])*2 + a[1+(n-2)//2]*(n & 1)
      print(res)
    
    @staticmethod
    def e():
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
 

  class ABC174:
    @staticmethod
    def a():
      print('Yes' if int(sys.stdin.readline().rstrip())>=30 else 'No')


  class ACL001:
    @staticmethod 
    def a():
      n, *xy = map(int, sys.stdin.read().split())
      *xy, = zip(*[iter(xy)]*2)
      print(xy)
      pass




  class MSolutions2020:
    @staticmethod
    def a():
      x = int(sys.stdin.readline().rstrip())
      x -= 400
      print(8-x//200)
    
    @staticmethod
    def b():
      r, g, b, k = map(int, sys.stdin.read().split())
      while k and g <= r:
        g *= 2
        k -= 1
      while k and b <= g:
        b *= 2
        k -= 1
      print('Yes' if r < g < b else 'No')
    
    @staticmethod
    def c():
      n, k, *a = map(int, sys.stdin.read().split())
      for i in range(k, n):
        print('Yes' if a[i] > a[i-k] else 'No')
    
    @staticmethod
    def d():
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



class Codeforces:
  pass 

class ProjectEuler:
  @staticmethod
  def p1():
    def f(n, x):
      return (x + n//x*x) * (n//x) // 2
    n = 1000
    ans = f(n-1, 3)+f(n-1, 5)-f(n-1, 15)
    print(ans)

  @staticmethod
  def p2():
    fib = [1, 2]
    while fib[-1] < 4*10**6:
      fib.append(fib[-1]+fib[-2])
    print(sum(fib[1:-1:3]))

  @staticmethod
  def p3():
    pn = NumberTheory.PrimeNumbers()
    res = pn.factorize(600851475143)
    print(max(res.keys()))

  @staticmethod
  def p4():
    def is_palindrome(n):
      n = str(n)
      return n == n[::-1]
    cand = []
    for a in range(100, 1000):
      for b in range(a, 1000):
        n = a*b 
        if is_palindrome(n): cand.append(n)
    print(max(cand))

  @staticmethod
  def p5():
    pn = NumberTheory.PrimeNumbers()
    res = defaultdict(int)
    for i in range(1, 21):
      for p, c in pn.factorize(i).items():
        res[p] = max(res[p], c)
    ans = 1
    for p, c in res.items(): ans *= pow(p, c)
    print(ans)

  @staticmethod
  def p6():
    a = np.arange(101)
    b = np.cumsum(a**2)
    a = a.cumsum()
    print(a[100]**2 - b[100])

  @staticmethod
  def p7():
    nt = NumberTheory.PrimeNumbers()
    print(sorted(nt)[10000])
  @staticmethod
  def p8():
    n = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    n = [int(d) for d in list(n)]
    res = 0
    for i in range(988):
      x = 1
      for j in range(13):
        x *= n[i+j]
      res = max(res, x)
    print(res)
  @staticmethod
  def p9():
    for a in range(1, 997):
      for b in range(a, 998-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
          print(a*b*c)
          return
  @staticmethod
  def p10():
    pn = NumberTheory.PrimeNumbers(2*10**6+1)
    print(sum(pn))
  @staticmethod
  def p11():
    grid = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
    # grid = np.array(grid.split(), dtype=np.int64).reshape(20, -1)
    # cand = []
    # for i in range(20):
    #   bl1 = i+3 < 20
    #   for j in range(20):
    #     bl2 = j+3 < 20
    #     if bl1:
    #       np.prod
    #       tmp = 1
    #       for d in range(4):
    #         tmp *= grid[i+d, j]
    print(grid)
  
  pass 

class Yukicoder:
  def __init__(self):
    pass

  def __call__(self):
    print(1)


if __name__ == '__main__':
  AtCoder.ABC014.d()

