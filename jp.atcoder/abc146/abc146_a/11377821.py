import sys

day = 'SUN, MON, TUE, WED, THU, FRI, SAT'.split(', ')
table = dict(zip(day, range(7, 0, -1)))

s = sys.stdin.readline().rstrip()

def main():
    print(table[s])

if __name__ ==  '__main__':
    main()
