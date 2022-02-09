import sys

a, b = map(int, sys.stdin.readline().split())
if b > a:
    a, b = b, a

def main():
    if a == b: res = a * 2
    else: res = a * 2 - 1
    print(res)

if __name__ ==  '__main__':
    main()
