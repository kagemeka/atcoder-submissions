import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    cur = 1
    cnt = 0
    while cur < b:
        cnt += 1
        cur += a - 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
