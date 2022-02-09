# 2019-11-24 16:35:46(JST)
import sys
import numpy as np

def main():
    S = sys.stdin.read().split()

    count = 0
    for s in S:
        if 'r' in s:
            count += 1

    print(count)



if __name__ == '__main__':
    main()
