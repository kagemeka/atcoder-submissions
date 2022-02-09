import sys

*a = map(int, sys.stdin.readline().split())

def main():
    return max(a) - min(a)

if __name__ == '__main__':
    ans = main()
    print(ans)
