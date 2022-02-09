import sys

def main():
    *E, = map(int, sys.stdin.readline().split())
    B, *L = map(int, sys.stdin.read().split())

    cnt = 0
    bonus = False
    for i in range(6):
        if L[i] == E[i]:
            cnt += 1
        elif L[i] == B:
            bonus = True

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
