import sys

y, m, d = map(int, sys.stdin.readline().split('/'))

def main():
    return 'Heisei' if m <= 4 else 'TBD'

if __name__ == '__main__':
    ans = main()
    print(ans)
