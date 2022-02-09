import sys
from string import digits

def main():
    n, s = sys.stdin.read().split()

    cnt = 0
    for i in digits:
        x = s.find(i)
        if x == -1:
            continue
        for j in digits:
            y = s.find(j, x + 1)
            if y == -1:
                continue
            for k in digits:
                z = s.find(k, y + 1)
                if z == -1:
                    continue
                cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
