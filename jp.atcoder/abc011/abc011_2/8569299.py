# 2019-11-23 18:41:55(JST)
import sys

def main():
    s = sys.stdin.readline().rstrip()
    s = s[0].upper() + s[1:].lower()
    print(s)

if __name__ == '__main__':
    main()
