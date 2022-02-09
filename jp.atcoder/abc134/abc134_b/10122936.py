import sys

n, d = map(int, sys.stdin.readline().split())

def main():
    c = 2*d + 1
    return (n + c - 1) // c

if __name__ == '__main__':
    ans = main()
    print(ans)
