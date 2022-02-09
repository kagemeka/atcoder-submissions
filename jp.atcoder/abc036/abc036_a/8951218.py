import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = (b + a - 1) // a
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
