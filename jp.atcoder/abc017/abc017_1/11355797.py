import sys

se = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    res = 0
    for s, e in se:
        res += s // 10 * e
    print(res)

if __name__ ==  '__main__':
    main()
