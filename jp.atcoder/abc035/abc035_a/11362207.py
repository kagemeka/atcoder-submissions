import sys

w, h = map(int, sys.stdin.readline().split())

def main():
    ans = '4:3' if (w + h*2) / w == 2.5 else '16:9'
    print(ans)

if __name__ ==  '__main__':
    main()
