import sys

a = sorted([int(x) for x in sys.stdin.readline().split()])

def main():
    d = a[-1] * 2 - a[0] - a[1]
    if d & 1: d += 3
    print(d // 2)

if __name__ ==  '__main__':
    main()
