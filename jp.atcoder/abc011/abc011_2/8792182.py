import sys
s = sys.stdin.readline().rstrip()

def main():
    t = s[0].upper() + s[1:].lower()
    print(t)

if __name__ == '__main__':
    main()
