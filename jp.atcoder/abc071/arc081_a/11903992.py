import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    a.sort()
    y = x = 0
    i = n - 1
    while i > 0:
        if a[i] == a[i-1]:
            if not y:
                y = a[i]
                i -= 1
            else:
                x = a[i]
                break
        i -= 1
    print(y * x)

if __name__ ==  '__main__':
    main()
