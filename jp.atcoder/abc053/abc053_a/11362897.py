import sys

x = int(sys.stdin.readline().rstrip())

def main():
    ans = 'ABC' if x < 1200 else 'ARC'
    print(ans)

if __name__ ==  '__main__':
    main()
