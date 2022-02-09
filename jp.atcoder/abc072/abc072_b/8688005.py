import sys

def main():
    s = sys.stdin.readline().rstrip()
    res = s[::2]
    print(res)

if __name__ == '__main__':
    main()
