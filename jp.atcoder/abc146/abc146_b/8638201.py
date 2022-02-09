# 2019-11-24 20:59:47(JST)
import sys
from string import ascii_uppercase as alphabet

# alpha_num = dict((alpha, num) for num, alpha in enumerate(alphabet, 0))
alpha_ind = dict((alphabet[i], i) for i in range(26))

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    t = ''
    for char in s:
        t += alphabet[(alpha_num[char] + n) % 26]

    print(t)

if __name__ == '__main__':
    main()
