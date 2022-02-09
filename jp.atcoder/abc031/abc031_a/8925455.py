import sys

a, d = map(int, sys.stdin.readline().split())

def main():
    if a <= d:
        a += 1
    else:
        b += 1
    return a * b

if __name__ == '__main__':
    ans = main()
    print(ans)
