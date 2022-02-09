import sys
from string import digits

def main():
    n, s = sys.stdin.read().split()

    res = []
    for i in digits:
        x = s.find(i)
        if x == -1:
            continue
        for j in digits:
            y = s.find(j, x+1)
            if y == -1:
                continue
            for k in digits:
                if k in s[y+1:]:
                    res.append((i, j, k))

    print(len(res))

if __name__ == '__main__':
    main()
