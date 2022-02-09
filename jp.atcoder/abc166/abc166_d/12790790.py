import sys

def divisors(n):
  res = set()
  for i in range(1, int(n ** 0.5) + 1):
    if n % i: continue
    res.add(i)
    res.add(n // i)
  return res

x = int(sys.stdin.readline().rstrip())

def f(a, b): return pow(a, 5) - pow(b, 5)

def ternary_search(d):
    lo, hi = -1, 10 ** 18
    while lo + 1 < hi:
        a = (lo + hi) // 2
        b = a - d
        bl = a >= abs(b)
        bl2 = f(a, b) >= x
        if bl ^ bl2: lo = a
        else: hi = a
    return hi, hi - d

def main():
    diffs = divisors(x)
    for d in diffs:
        a, b = ternary_search(d)
        if f(a, b) == x:
            print(a, b)
            return

if __name__ == '__main__':
    main()
