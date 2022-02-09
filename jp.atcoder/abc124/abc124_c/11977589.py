import sys

s = sys.stdin.readline().rstrip()

def main():
    c1 = s[::2].count('1') + s[1::2].count('0')
    c2 = s[::2].count('0') + s[1::2].count('1')
    print(min(c1, c2))

if __name__ ==  '__main__':
    main()
