import sys

n, a, b = map(int, sys.stdin.readline().split())

def main():
    c = a + b
    q, r = divmod(n, c)
    res = a * q + min(a, r)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
