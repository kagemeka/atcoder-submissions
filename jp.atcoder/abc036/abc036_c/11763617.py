import sys

n, *a = map(int, sys.stdin.read().split())
a = sorted(enumerate(a), key=lambda x: x[1])

def main():
    b = [None] * n
    i = -1
    prev = -1
    for j, x in a:
        if x != prev: i += 1
        b[j] = i
        prev = x
    print(*b, sep='\n')

if __name__ ==  '__main__':
    main()
