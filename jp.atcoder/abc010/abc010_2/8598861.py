# 2019-11-24 13:14:50(JST)
import sys
# import numpy as np

def main():
    n, *a = map(int, sys.stdin.read().split())

    count = 0
    for petal in a:
        ok = False
        while not ok:
            if petal % 2 == 0 or petal % 6 == 5:
                petal -= 1
                count += 1
            else:
                ok = True
    print(count)

if __name__ == '__main__':
    main()
