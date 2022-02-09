# 2019-11-24 12:12:53(JST)
import sys
# import numpy as np

def main():
    a, b = map(int, sys.stdin.read().split())

    if 0 < a:
        ans = 'Positive'
    elif 0 <= b:
        ans = 'Zero'
    else:
        if (b - a + 1) % 2 == 0:
            ans = 'Positive'
        else:
            ans = 'Negative'

    print(ans)

if __name__ == '__main__':
    main()
