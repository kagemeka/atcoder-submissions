import sys

n, k, m, *a = map(int, sys.stdin.read().split())

def main():
    s = sum(a)
    target = m * n
    res = target - s
    return -1 if res > k else max(0, res)

if __name__ == '__main__':
    ans = main()
    print(ans)
