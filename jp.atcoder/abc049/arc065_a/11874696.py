import sys

t = set('dream, dreamer, erase, eraser'.split(', '))

def obtainable(s):
  while True:
    if s[-5:] in t:
      s = s[:-5]
    elif s[-6:] in t:
      s = s[:-6]
    else:
      return False
    if not s:
      return True

s = sys.stdin.readline().rstrip()

def main():
  print("YES" if obtainable(s) else "NO")

if __name__ ==  '__main__':
  main()
