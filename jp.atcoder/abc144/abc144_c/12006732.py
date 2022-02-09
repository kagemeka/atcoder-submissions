import sys

def divisors(n):
  res = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i: continue
    res.append(i)
    res.append(n // i)
  return res

n = int(sys.stdin.readline().rstrip())

def main():
    res = divisors(n)
    print(res[-1] + res[-2] - 2)

if __name__ ==  '__main__':
    main()
