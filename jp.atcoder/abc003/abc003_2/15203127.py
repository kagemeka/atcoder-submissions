import sys

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
  pass


def D():
  pass



if __name__ == "__main__":
  # A()
  B()
  C()
  D()
