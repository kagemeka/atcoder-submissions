import sys

*a, = map(int, sys.stdin.read().split())

def main():
    res = [None] * 3
    b = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
    for i in range(3):
        res[b[i][0]] = i + 1
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
