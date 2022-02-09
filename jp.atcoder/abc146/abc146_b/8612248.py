# 2019-11-24 20:59:47(JST)
import sys
# import numpy as np
from string import ascii_uppercase as alphabet

alphabet = alphabet[-1] + alphabet[0:]

alpha_num = enumerate(alphabet, 0)

alpha_num = dict((alpha, num) for num, alpha in alpha_num)

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    t = ''
    for c in s:
        t += alphabet[(alpha_num[c] + n) % 26]

    print(t)


if __name__ == '__main__':
    main()
