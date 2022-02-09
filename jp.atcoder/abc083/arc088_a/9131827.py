import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    a = x
    cnt = 0
    while a <= y:
        cnt += 1
        a *= 2
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
