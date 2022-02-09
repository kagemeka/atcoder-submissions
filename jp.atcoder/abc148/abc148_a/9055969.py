import sys

a, b = map(int, sys.stdin.read().split())

def main():
    ans = 6 - a - b
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
