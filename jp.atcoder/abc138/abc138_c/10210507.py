import sys

n, *v = map(int, sys.stdin.read().split())

def main():
    v.sort(reverse=True)
    res = 0
    for i in range(n-1):
        res += v[i] / 2 ** (i + 1)
    res += v[-1] / 2 ** (n - 1)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
