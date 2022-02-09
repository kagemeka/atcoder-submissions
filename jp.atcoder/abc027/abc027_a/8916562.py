import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    if a == b:
        return c
    elif b == c:
        return a
    else:
        return b

if __name__ == '__main__':
    ans = main()
    print(ans)
