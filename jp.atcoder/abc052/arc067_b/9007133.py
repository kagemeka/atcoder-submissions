import sys

n, a, b, *x = map(int, sys.stdin.read().split())

def main():
    border = (b + a - 1) // a

    res = 0
    for i in range(n-1):
        d = x[i+1] - x[i]
        if d >= border:
            res += b
        else:
            res += a * d

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
