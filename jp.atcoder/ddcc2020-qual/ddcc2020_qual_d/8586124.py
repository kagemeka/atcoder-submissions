# 2019-11-23 21:00:35(JST)
import sys

def main():
    m = int(sys.stdin.readline().rstrip())

    s = ''
    for i in range(m):
        d, c = sys.stdin.readline().split()
        c = int(c)
        s += d * c

    count = 0
    while len(s) >= 2:
        s = str(int(s[0]) + int(s[1])) + s[2:]
        count += 1

    print(count)




if __name__ == '__main__':
    main()
