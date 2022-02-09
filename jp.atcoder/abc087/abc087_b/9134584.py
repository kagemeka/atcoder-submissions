import sys

a, b, c, x = map(int, sys.stdin.read().split())
x //= 50

def main():
    ways = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if 10*i + 2*j + k == x:
                    ways += 1
    return ways

if __name__ == '__main__':
    ans = main()
    print(ans)
