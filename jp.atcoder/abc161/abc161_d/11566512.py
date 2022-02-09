import sys

k = int(sys.stdin.readline().rstrip())

def main(k):
    if k <= 9:
        print(k)
        return
    res = list(range(1, 10))
    k -= 9
    while True:
        nex = []
        for n in res:
            r = n % 10
            n *= 10
            for i in range(-1, 2):
                if 0 <= r + i <= 9:
                    nex.append(n + r + i)
                    k -= 1
                    if not k:
                        print(nex[-1])
                        return
        res = nex.copy()

if __name__ == '__main__':
    main(k)
