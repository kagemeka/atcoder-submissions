import sys
def main():
    n, *log = sys.stdin.read().split()

    used = set()
    last = log[0][-1]
    used.add(log[0])
    for i in range(1, int(n)):
        w = log[i]
        if w[0] != last or w in used:
            if i % 2 != 0:
                res = 'WIN'
            else:
                res = 'LOSE'
            break
    else:
        res = 'DRAW'

    print(res)

if __name__ == '__main__':
    main()
