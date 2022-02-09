import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    return max(c + b - a, 0)

if __name__ == '__main__':
    ans = main()
    print(ans)
