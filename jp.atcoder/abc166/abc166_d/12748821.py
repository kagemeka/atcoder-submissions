import sys

def divisors(n):
  res = set()
  for i in range(1, int(n ** 0.5) + 1):
    if n % i: continue
    res.add(i)
    res.add(n // i)
  return res

x = int(sys.stdin.readline().rstrip())

def f(a, b):
    return pow(a, 5) - pow(b, 5)

def binary(d):
    lo, hi = 0, 10 ** 9
    while lo + 1 < hi:
        a = (lo + hi) // 2
        b = a - d
        if f(a, b) >= x:
            hi = a
        else:
            lo = a
    return hi, hi - d

def main():
    diffs = divisors(x)
    for d in diffs:
        a, b = binary(d)
        if f(a, b) == x:
            print(a, b)
            return

if __name__ == '__main__':
    main()
