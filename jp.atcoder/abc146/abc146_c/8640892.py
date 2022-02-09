import sys

def main():
    a, b, x = map(int, sys.stdin.readline().split())

    if x >= a * 10 ** 9 + b * 10:
        print(10 ** 9)
        sys.exit()
    elif x < a + b:
        print(0)
        sys.exit()

    cand = []
    for l in range(1, 10): # length
        n = (x - b * l) / a
        if 10 ** (l - 1) <= n < 10 ** l:
            cand.append(n)

    if cand:
        print(max(cand))





if __name__ == '__main__':
    main()
