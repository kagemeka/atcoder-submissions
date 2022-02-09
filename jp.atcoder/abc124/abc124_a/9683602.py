import sys

a, b = map(int, sys.stdin.readline().split())
if a > b: a, b = b, a

def main():
    return b * 2 if a == b else b * 2 - 1

if __name__ == '__main__':
    ans = main()
    print(ans)
