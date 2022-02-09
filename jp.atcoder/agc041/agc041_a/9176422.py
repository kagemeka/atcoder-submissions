import sys

n, a, b = map(int, sys.stdin.readline().split())

def main(a, b):
    d = b - a
    if d % 2 == 0:
        return d // 2

    if n - b >= abs(1 - a):
        res = a
        b -= res
        a = 1
    else:
        res = n - b + 1
        a += res
        b = n

    return res

if __name__ == '__main__':
    ans = main(a, b)
    print(ans)
