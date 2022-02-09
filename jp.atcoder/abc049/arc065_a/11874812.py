import sys

t = set('dream, dreamer, erase, eraser'.split(', '))

def obtainable(s):
  while True:
    for i in range(5, 8):
      if s[-i:] in t:
        s = s[:-i]
        break
    else:
      return False
    if not s:
      return True

s = sys.stdin.readline().rstrip()

def main():
  print(t)
  print("YES" if obtainable(s) else "NO")

if __name__ ==  '__main__':
  main()
