import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yay!' if a <= 8 and b <= 8 else ':('
    print(ans)

if __name__ ==  '__main__':
    main()
