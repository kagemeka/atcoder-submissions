import sys

def A():
  n = sys.stdin.readline().rstrip()
  if '3' in n:
    print('YES')
  elif int(n)%3 == 0:
    print('YES')
  else:
    print('NO')


def B():
  mod = 10007
  t = [0, 0, 1]
  for _ in range(1001001):
    t.append(t[-1]+t[-2]+t[-3])
    t[-1] %= mod

  n = int(sys.stdin.readline().rstrip())
  print(t[n-1])


def C():
  n, m = map(int, sys.stdin.readline().split())

  cnt = [0, 0, 0]
  if m == 1:
    cnt = [-1, -1, -1]
  else:
    if m & 1:
      m -= 3; cnt[1] += 1; n -= 1
    cnt[2] = m//2 - n
    cnt[0] = n - cnt[2]
  if cnt[0]<0 or cnt[1]<0 or cnt[2]<0:
    print(-1, -1, -1)
  else:
    print(*cnt, sep=' ')


from bisect import bisect_left as bi_l
def D():
  n, *c = map(int, sys.stdin.read().split())
  inf = float('inf')
  lis = [inf]*n
  for x in c:
    lis[bi_l(lis, x)] = x
  print(n - bi_l(lis, inf))


if __name__ == "__main__":
  # A()
  # B()
  # C()
  D()
