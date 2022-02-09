import sys

n, k, *r = map(int, sys.stdin.read().split())
r = sorted(r)[n-k:]

def main():
    rate = 0
    for i in r:
        rate = (rate + i) / 2
    return rate

if __name__ == '__main__':
    ans = main()
    print(ans)
