import sys
from datetime import date, timedelta

def main():
    y, m, d = map(int, sys.stdin.readline().rstrip().split('/'))
    d = date(y, m, d)

    while d.year % (d.month * d.day) != 0:
        if d.day == 1:
            d += timedelta(days=28)
        else:
            d += timedelta(days=1)

    print(str(d).replace('-', '/'))

if __name__ == '__main__':
    main()
