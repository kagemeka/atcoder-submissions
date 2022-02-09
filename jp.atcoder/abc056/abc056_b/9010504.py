import sys

w, a, b = map(int, sys.stdin.readline().split())

def main():
    if a + w < b:
        return b - (a + w)
    elif b + w < a:
        return a - (b + w)
    else:
        return 0

if __name__ == '__main__':
    ans = main()
    print(ans)
