import sys

a, p = map(int, sys.stdin.readline().split())

def main():
    res = (3 * a + p) // 2
    print(res)

if __name__ ==  '__main__':
    main()
