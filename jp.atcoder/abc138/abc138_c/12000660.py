import sys

n, *v = map(int, sys.stdin.read().split())
v.sort()

def main():
    res = v[0]
    for i in range(1, n):
        res = (res + v[i]) / 2
    print(res)

if __name__ ==  '__main__':
    main()
