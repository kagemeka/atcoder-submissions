import sys

n, k, *a = map(int, sys.stdin.read().split())

def main():
    for i in range(n - 1):
        a[i+1] += a[i]
    s = sum(a[-(n-k+1):]) - sum(a[:n-k])
    print(s)

if __name__ ==  '__main__':
    main()
