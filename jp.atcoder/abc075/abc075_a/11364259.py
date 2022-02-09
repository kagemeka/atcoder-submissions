import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    if a == b: ans = c
    elif b == c: ans = a
    else: ans = b
    print(ans)

if __name__ ==  '__main__':
    main()
