import sys

a, s = sys.stdin.read().split()
a = int(a)

def main():
    ans = 'red' if a < 3200 else s
    print(ans)

if __name__ ==  '__main__':
    main()
