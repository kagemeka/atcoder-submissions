import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = (a + b) % 24
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
