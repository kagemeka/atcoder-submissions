# 2019-11-25 15:34:15(JST)
import sys
def main():
    x, y = map(int, sys.stdin.readline().split())

    if y == 0:
        if x > 0:
            ans = x + 1
        else:
            ans = -x
    elif y > 0:
        if x > y:
            ans = x - y + 2
        elif x >= 0:
            ans = y - x
        else:
            ans = abs(y + x) + 1
    else:
        if x >= 0:
            ans = abs(y + x) + 1
        elif x > y:
            ans = x - y + 2
        else:
            ans = y - x

    print(ans)

if __name__ == '__main__':
    main()
