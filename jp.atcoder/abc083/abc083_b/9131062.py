import sys

n, a, b = map(int, sys.stdin.readline().split())

def main():
    res = 0
    for i in range(1, n+1):
        s = sum([int(d) for d in str(i)])
        if a <= s <= b:
            res += i
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
