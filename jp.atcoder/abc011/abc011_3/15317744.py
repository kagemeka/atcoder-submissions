import sys
import numpy as np
from heapq import heappush, heappop
from bisect import bisect_left as bi_l, bisect_right as bi_r
from collections import deque, Counter, defaultdict
from itertools import combinations, product
inf = float('inf')
MOD = 10**9+7
# MOD = 998244353


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
    inf = float('inf')
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

if __name__ == '__main__':
  ABC011.C()
