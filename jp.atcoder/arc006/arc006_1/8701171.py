import sys

def main():
    *E, = map(int, sys.stdin.readline().split())
    B, *L = map(int, sys.stdin.read().split())

    E = set(E)
    L = set(L)
    cnt = len(E & L)
    if B in L:
        bonus = True
    else:
        bonus = False

    if cnt == 6:
        res = 1
    elif cnt == 5:
        if bonus:
            res = 2
        else:
            res = 3
    elif cnt == 4:
        res = 4
    elif cnt == 3:
        res = 5
    else:
        res = 0

    print(res)

if __name__ == '__main__':
    main()
