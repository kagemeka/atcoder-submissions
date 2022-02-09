import sys
import datetime

def main():
    y, m, d = map(int, sys.stdin.readline().rstrip().split('/'))
    date = datetime.date(y, m, d)

    while date.year % (date.month * date.day) != 0:
        if date.day == 1:
            date += datetime.timedelta(months=1)
        else:
            date += datetime.timedelta(days=1)

    print(str(date).replace('-', '/'))

if __name__ == '__main__':
    main()
