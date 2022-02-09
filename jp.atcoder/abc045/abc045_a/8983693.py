import sys

a, b, h = map(int, sys.stdin.read().split())

def main():
    ans = (a + b) * h // 2
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
