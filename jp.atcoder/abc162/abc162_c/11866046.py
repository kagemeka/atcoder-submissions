import sys

def gcd(a, b): return gcd(b, a % b) if b else abs(a)

k = int(sys.stdin.readline().rstrip())

def main():
  res = 0
  cnt = [0] * (k + 1)
  for i in range(1, k + 1):
    for j in range(1, k + 1):
      cnt[gcd(i, j)] += 1
  for i in range(1, k + 1):
    for j in range(1, k + 1):
      res += gcd(i, j) * cnt[i]
  print(res)

if __name__ ==  '__main__':
    main()
