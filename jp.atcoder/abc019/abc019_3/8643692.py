# 2019-11-25 12:34:24(JST)
import sys
def main():
    n, *a = map(int, sys.stdin.read().split())
    # aの各要素を奇数になるまで割り続けて、残った奇数の種類が答え
    res = set()
    for j in a:
        while j % 2 == 0:
            j //= 2
        res.add(j)

    print(len(res))

if __name__ == '__main__':
    main()
