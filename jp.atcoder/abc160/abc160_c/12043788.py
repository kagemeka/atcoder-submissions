import sys

k, n, *a = map(int, sys.stdin.read().split())
a += [a[0] + k]

def main():
    d = [a[i+1] - a[i] for i in range(n)]
    print(k - max(d))

if __name__ ==  '__main__':
    main()
