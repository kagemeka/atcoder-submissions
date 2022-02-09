import sys

x = int(sys.stdin.readline().rstrip())

def main():
  q, r = divmod(x, 11)
  res = q * 2
  if r: res += 1
  if r > 6: res += 1
  print(res)

if __name__ ==  '__main__':
  main()
