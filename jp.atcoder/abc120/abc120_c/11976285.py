import sys

s = sys.stdin.readline().rstrip()
n = len(s)

def main():
    c = s.count('0')
    print(min(n-c, c) * 2)

if __name__ ==  '__main__':
    main()
