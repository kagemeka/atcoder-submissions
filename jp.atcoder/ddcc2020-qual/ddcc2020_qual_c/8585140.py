# 2019-11-23 21:00:35(JST)
import sys

def main():
    H, W, K = map(int, sys.stdin.readline().split())
    s = ['.' * (W+1)] + ['.' + sys.stdin.readline().rstrip() for _ in range(H)]


    res = [[None for _ in range(W + 2)]] + [[None] + [0 for _ in range(W)] + [None] for _ in range(H)] + [[None for _ in range(W + 2)]]

    number = 1
    for i in range(1, H+1):
        if not '#' in s[i]:
            continue
        else:
            j = 1
            while j <= W:
                res[i][j] = number
                if s[i][j] == '#':
                    res[i][j] = number
                    if '#' in s[i][j+1:]:
                        number += 1
                j += 1
            number += 1

    for i in range(1, H+1):
        if res[i][1] == 1:
            count = i
            break

    for i in range(1, count):
        res[i] = res[count]

    for i in range(1, H):
        if res[i+1][1] == 0:
            res[i+1] = res[i]

    for i in range(1, H+1):
        print(' '.join(map(str, res[i][1:W+1])))






if __name__ == '__main__':
    main()
