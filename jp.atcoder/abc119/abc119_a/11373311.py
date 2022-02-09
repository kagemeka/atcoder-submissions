import sys

y, m, d = map(int, sys.stdin.readline().rstrip().split('/'))

def main():
    ans = 'Heisei' if m <= 4 else 'TBD'
    print(ans)

if __name__ ==  '__main__':
    main()
