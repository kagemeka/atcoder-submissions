import sys

n = int(sys.stdin.readline().rstrip())
a = [0] + [int(x) for x in sys.stdin.readline().split()]
b = [0] + [int(x) for x in sys.stdin.readline().split()]

def main():
    for i in range(n):
        a[i+1] += a[i]
        b[i+1] += b[i]
    res = 0
    for i in range(1, n + 1):
        res = max(res, a[i] + b[n] - b[i-1])
    print(res)

if __name__ ==  '__main__':
    main()
