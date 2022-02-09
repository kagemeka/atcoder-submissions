import sys

a, b, x = map(int, sys.stdin.readline().split())

def main():
    ans = b // x - (a - 1) // x
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
