import sys

n, r = map(int, sys.stdin.readline().split())

def main():
    res = r + 100 * max(10 - n, 0)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
