import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    if a >= 13: c = b
    elif a >= 6: c = b // 2
    else: c = 0
    print(c)

if __name__ ==  '__main__':
    main()
