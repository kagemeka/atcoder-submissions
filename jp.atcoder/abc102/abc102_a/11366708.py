import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = n
    if n & 1: ans *= 2
    print(ans)

if __name__ ==  '__main__':
    main()
