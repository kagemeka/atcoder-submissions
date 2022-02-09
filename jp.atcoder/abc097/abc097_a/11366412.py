import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    ans = 'No'
    if abs(c - a) <= d: ans = 'Yes'
    elif abs(b - a) <= d and abs(c - b) <= d: ans = 'Yes'
    print(ans)

if __name__ ==  '__main__':
    main()
