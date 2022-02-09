import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    i = b - a - 1
    return (1 + i) * i // 2 - a

if __name__ == '__main__':
    ans = main()
    print(ans)
