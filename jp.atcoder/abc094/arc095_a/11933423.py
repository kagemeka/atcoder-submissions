import sys

n, *x = map(int, sys.stdin.read().split())

def main():
    a = sorted(x)
    l = a[n//2-1]; r = a[n//2]
    for i in range(n):
        print(l if x[i] >= r else r)

if __name__ ==  '__main__':
    main()
