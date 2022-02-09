import sys

n, k, *a = map(int, sys.stdin.read().split())
a = [0] + a

def main():
    for i in range(n):
        a[i+1] += a[i]
    s = 0
    for i in range(n-k+1):
        s += a[i+k] - a[i]
    print(s)

if __name__ ==  '__main__':
    main()
