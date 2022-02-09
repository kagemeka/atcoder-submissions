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
  pass


def D():
  pass


if __name__ == "__main__":
  # A()
  B()
  C()
  D()
