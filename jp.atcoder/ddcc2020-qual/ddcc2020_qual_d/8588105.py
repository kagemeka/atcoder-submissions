# 2019-11-23 21:00:35(JST)
import sys

def main():
    m = int(sys.stdin.readline().rstrip())

    res = []

    total = 0
    for i in range(m):
        d, c = sys.stdin.readline().split()
        s = d
        count = 0
        for _ in range(int(c)-1):
            s = str(int(s) + int(d))
            count += 1
            if len(s) == 2:
                s = str(int(s[0]) + int(s[1]))
                count += 1
        total += count
        res.append(s)


    s = res[0]
    for i in range(1, m):
        s = str(int(s) + int(res[i]))
        total += 1
        if len(s) == 2:
            s = str(int(s[0]) + int(s[1]))
            total += 1
    print(total)


if __name__ == '__main__':
    main()
