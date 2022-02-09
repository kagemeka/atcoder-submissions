# 2019-11-23 21:00:35(JST)
import sys

def main():
    m = int(sys.stdin.readline().rstrip())

    S = ''

    total = 0
    for i in range(m):
        d, c = sys.stdin.readline().split()
        c = int(c)
        s = d * c
        count = 0
        while len(s) >= 2:
            s = str(int(s[0]) + int(s[1])) + s[2:]
            count += 1
        total += count
        S += s


    while len(S) >= 2:
        S = str(int(S[0]) + int(S[1])) + S[2:]
        total += 1

    print(total)


if __name__ == '__main__':
    main()
