import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    return max(x, y)

if __name__ == '__main__':
    ans = main()
    print(ans)
