# 2019-11-25 12:34:24(JST)
import sys
def main():
    s = sys.stdin.readline().rstrip()

    res = []
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
        else:
            res.append((s[i], str(count)))
            count = 1

    res.append((s[-1], str(count)))

    print(''.join([''.join((char, count)) for char, count in res]))

if __name__ == '__main__':
    main()
