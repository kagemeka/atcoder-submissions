import sys

n = int(sys.stdin.readline().rstrip())
*p, = map(int, sys.stdin.readline().split())
*q, = map(int, sys.stdin.readline().split())

factorial = [1] * (n + 1)
for i in range(n): factorial[i+1] = factorial[i] * (i + 1)

def main():
    d = 0
    a = [0] * (n + 1); b = [0] * (n + 1)
    for i in range(n - 1):
        a[p[i]] = b[q[i]] = 1
        c1 = c2 = 0
        for j in range(1, p[i]): c1 += a[j]
        for j in range(1, q[i]): c2 += b[j]
        d += ((q[i] - c2) - (p[i] - c1)) * factorial[n-(i+1)]
    print(abs(d))

if __name__ ==  '__main__':
    main()
