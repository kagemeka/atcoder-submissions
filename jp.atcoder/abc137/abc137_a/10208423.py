import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return max(a+b, a-b, a*b)

if __name__ == '__main__':
    ans = main()
    print(ans)
