# 2019-11-26 17:11:55(JST)
import sys
from string import ascii_lowercase as alph
ind_alph = dict((char, ind) for ind, char in enumerate(alph))

def main():
    s, k = sys.stdin.read().split()
    s = list(s)
    k = int(k)
    n = len(s)

    i = 0
    while k:
        diff = (26 - ind_alph[s[i]]) % 26
        if diff <= k:
            s[i] = 'a'
            k -= diff
        if i == n - 1 and k:
                s[i] = alph[(ind_alph[s[i]] + k) % 26]
                k = 0
        i += 1

    print(''.join(s))

if __name__ == '__main__':
    main()
