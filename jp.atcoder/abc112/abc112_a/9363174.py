import sys

n = int(sys.stdin.readline().rstrip())
if n == 2:
    a, b = map(int, sys.stdin.read().split())

def main():
    return 'Hello World' if n == 1 else a + b

if __name__ == '__main__':
    ans = main()
    print(ans)
