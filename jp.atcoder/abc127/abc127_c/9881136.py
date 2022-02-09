import sys

n, m, *lr = map(int, sys.stdin.read().split())
l, r = lr[::2], lr[1::2]

def main():
    ans = max(min(r) - max(l) + 1, 0)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
