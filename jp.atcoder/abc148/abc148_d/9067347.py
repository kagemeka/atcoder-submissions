import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    x = 1
    for i in range(n):
        if a[i] == x:
            x += 1

    ans = n - (x - 1)
    return -1 if ans == n else ans

if __name__ == '__main__':
    ans = main()
    print(ans)
