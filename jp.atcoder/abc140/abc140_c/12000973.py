import sys
inf = float('inf')

n, *b = map(int, sys.stdin.read().split())
b = [inf] + b + [inf]

def main():
    a = [min(b[i], b[i+1]) for i in range(n)]
    print(sum(a))

if __name__ ==  '__main__':
    main()
