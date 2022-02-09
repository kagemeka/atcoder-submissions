import sys

n, k, *a = map(int, sys.stdin.read().split())
a.append(n + a[0])

def main():
    d = 0
    for i in range(k):
        d = max(d, a[i+1] - a[i])
    res = n - d
    print(res)

if __name__ == "__main__":
    main()
