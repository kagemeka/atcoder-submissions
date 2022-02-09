import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    if a >= 13:
        return b
    elif a >= 6:
        return b // 2
    else:
        return 0

if __name__ == '__main__':
    ans = main()
    print(ans)
