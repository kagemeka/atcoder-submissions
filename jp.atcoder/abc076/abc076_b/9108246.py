import sys

n, k = map(int, sys.stdin.read().split())

def main():
    x = 1
    for _ in range(n):
        if x > k:
            x += k
        else:
            x *= 2
    return x

if __name__ == '__main__':
    ans = main()
    print(ans)
