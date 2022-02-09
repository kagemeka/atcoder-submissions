import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = 'ABD' if n >= 1000 else 'ABC'
    print(ans)

if __name__ ==  '__main__':
    main()
