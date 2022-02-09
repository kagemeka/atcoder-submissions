import sys

def divisors(n):
  res = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i: continue
    res.append(i)
  return res

n = int(sys.stdin.readline().rstrip())

def main():
    res = divisors(n)
    print(len(str(n // res[-1])))

if __name__ ==  '__main__':
    main()
