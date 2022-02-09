import sys

a, b = map(int, sys.stdin.readline().split())
if a < b: a, b = b, a

def main():
    r, c = 16 - b * 2, a - b
    ans = 'Yay!' if c <= r // 2 else ':('
    print(ans)

if __name__ ==  '__main__':
    main()
