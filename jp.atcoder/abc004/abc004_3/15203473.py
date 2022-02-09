import sys

def A():
  print(int(sys.stdin.readline().rstrip())*2)
  pass


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


def D():
  pass

if __name__ == "__main__":
  # A()
  # B()
  C()
  D()
