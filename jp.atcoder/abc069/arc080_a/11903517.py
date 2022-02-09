import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    c4 = c2 = 0
    for x in a:
        if not x % 4: c4 += 1
        elif not x % 2: c2 += 1
    ans = 'Yes' if c4 >= n // 2 or c4 * 2 + c2 >= n else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
