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


if __name__ == "__main__":
  # A()
  B()
