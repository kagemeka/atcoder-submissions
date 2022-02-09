import sys

n, *d = map(int, sys.stdin.read().split())

def main():
    d.sort()
    h = n // 2
    l = d[h-1]; r = d[h]
    return r - (l + 1) + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
