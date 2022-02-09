import sys

pair = dict(zip('ACGT', 'TGCA'))

b = sys.stdin.readline().rstrip()

def main():
    print(pair[b])

if __name__ ==  '__main__':
    main()
