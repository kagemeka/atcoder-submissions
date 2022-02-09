import sys

s = sys.stdin.readline().rstrip()

def main():
    cnt = 0
    for c in s:
        if c == 'o': cnt += 1

    cost = 700 + 100 * cnt
    print(cost)

if __name__ ==  '__main__':
    main()
