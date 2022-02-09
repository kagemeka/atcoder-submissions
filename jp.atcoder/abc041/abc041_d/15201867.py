import sys


def A():
  s, i = sys.stdin.read().split()
  i = int(i)
  print(s[i-1])

def B():
  MOD = 10**9+7
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

if __name__ == "__main__":
  # A()
  # B()
  # C()
  D()
