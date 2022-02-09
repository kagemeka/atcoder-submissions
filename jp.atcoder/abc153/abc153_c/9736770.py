import sys

n, k, *h = map(int, sys.stdin.read().split())

def main():
    h.sort(reverse=True)
    res = h[k:]
    return 0 if not res else sum(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
