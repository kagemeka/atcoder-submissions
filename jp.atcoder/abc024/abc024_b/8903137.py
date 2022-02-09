import sys

n, T, *t = map(int, sys.stdin.read().split())

def main():
    total = 0
    opened = t[0]
    will_close = opened + T
    for i in range(1, n):
        if t[i] >= will_close:
            total += will_close - opened
            opened = t[i]
        will_close = t[i] + T
    total += will_close - opened
    return total

if __name__ == '__main__':
    ans = main()
    print(ans)
