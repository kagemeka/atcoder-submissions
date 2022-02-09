import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    return sum(a) - n

if __name__ == '__main__':
    ans = main()
    print(ans)
