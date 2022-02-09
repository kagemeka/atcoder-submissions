import sys

def base_convert(n, b):
  if not n: return 0
  res = ''
  while n:
    n, r = divmod(n, b)
    if r < 0: n += 1; r -= b
    res += str(r)
  return int(res[::-1])

n = int(sys.stdin.readline().rstrip())

def main():
    print(base_convert(n, -2))

if __name__ ==  '__main__':
    main()
